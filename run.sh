function blog_update {
	wget -q --tries=10 --timeout=20 --spider http://google.com
	if [[ $? -eq 0 ]]; then
		git add .
		now=$(date)
		git commit -am "automated commit on $now"
		git push heroku master
		gxmessage "blog push successful"
		python ~/Codes/blog2/main.py
	else

		gxmessage -center 'OFFLINE, Unable to push blog updates, Retry in ->'\
		  -buttons "5 minutes":5,"10 minutes":10,"Not today":0 \
		  -geometry 400x100 \
		  -title "Blog Update";

		answer=$?;
		
            	if [ $answer -eq 0 ]; then
                	true
	        else
        	        sleep $(($answer))
			blog_update
        	fi				
	fi
}

blog_update
