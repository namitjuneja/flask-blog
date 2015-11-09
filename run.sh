function blog_update 
{
	wget -q --tries=10 --timeout=20 --spider http://google.com
	if [[ $? -eq 0 ]]; then
		python ~/Codes/blog2/main.py
		git add .
		now=$(date)
		git commit -am "automated commit on $now"
		git push heroku master
		gxmessage "blog push successful"
	else

		gxmessage -center \
		  -buttons "5 minutes":5,"10 minutes":10, "Not Today":0 \
		  -geometry 290x80 \
		  -OFFLINE; Unable to push blog updates; Retry in ->'

		answer=$?
		$a = 0
		
            	if [ "$answer" = "$a" ]; then
                	:
	        else
        	        sleep $(($answer * 60))
			blog_update
        	fi			
	fi
}


