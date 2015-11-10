import datetime, markdown, re
from flask import Flask, render_template, request, redirect
from flask_flatpages import FlatPages

FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

file_names = []
titles = {}
for i in pages:
	file_names.append(i.path)
	titles[str(i.path)] = i.meta["title"]

@app.route("/")
def index():
	return render_template('index.html', pages = pages)

@app.route("/new/")
def new():
	return render_template('new.html', pages=pages)

def cleanhtml(raw_html):
	cleanr =re.compile('<.*?>')
	cleantext = re.sub(cleanr,'', raw_html)
	return cleantext

@app.route("/gen/", methods=['GET', 'POST'])
def gen():
	now = datetime.datetime.now()
	date = str(now.year)+str('%02d' % now.month)+str('%02d' % now.day)+str('%02d' % now.hour)+str('%02d' % now.minute)
	date_formatted = now.strftime("%B %d, %Y")
	title = request.form["title"]
	content = request.form["content"]
	glimpse = " ".join( cleanhtml(markdown.markdown(content)).split()[:40] )
	top = request.form["top"]
	tag = request.form["tag"]
	print tag


	file = open("pages/" + str(date) + ".md", "w")
	file.write("title: " + title + "\n")
	file.write("glimpse: " + glimpse + "\n")
	if top:
		file.write("top: " + top + "\n")
	file.write("date: " + date_formatted + "\n\n")
	file.write(content)
	file.close()
	return redirect("/")

    
@app.route('/<path:path>/')
def page(path):
	dict = {}
	for i in range(0, len(file_names)):
		if path == file_names[i]:
			if i != 0:
				dict["prev_title"] = titles[file_names[i-1]] 
				dict["prev_path"] = file_names[i-1]
				dict["prev_disabled"] = ""
			else:
				dict["prev_title"] = "no older post"
				dict["prev_path"] = ""
				dict["prev_disabled"] = "button-disabled"

			if i != len(file_names)-1:
				dict["next_title"] = titles[file_names[i+1]] 
				dict["next_path"] = file_names[i+1]
				dict["next_disabled"] = ""
			else:
				dict["next_title"] = "no new post"
				dict["next_path"] = ""
				dict["next_disabled"] = "button-disabled"

	xyz = pages.get_or_404(path)
	return render_template('page.html', page=xyz, dict = dict)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

if __name__ == '__main__':
	app.run(port=8000, debug = True)