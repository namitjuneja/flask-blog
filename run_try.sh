gxmessage -center 'OFFLINE, Unable to push blog updates, Retry in ->'\
		  -buttons "5 minutes":5,"10 minutes":10,"Not today":0 \
		  -geometry 400x100 \
		  -title "Blog Update";

		answer=$?;
		echo $answer
		a=0
		
            	if [ "$answer" = "$a" ]; then
                	true
	        else
        	        sleep $(($answer))
			blog_update
        	fi	
