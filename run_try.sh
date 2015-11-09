function blog_update {
	wget -q --tries=10 --timeout=20 --spider http://google.com
	if [[ $? -eq 0 ]]; then

		gxmessage -center 'OFFLINE, Unable to push blog updates, Retry in ->'\
		  -buttons "5 minutes":5,"10 minutes":10,"Not today":0 \
		  -geometry 400x100 \
		  -title "Blog Update";

		answer=$?;
		a=0
		
            	if [ $answer -eq 0 ]; then
                	true
	        else
        	        sleep $(($answer))
			blog_update
        	fi				
	fi
}

blog_update
