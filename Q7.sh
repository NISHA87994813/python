echo -n "enter file1"
read fname
if [ -r$fname -a -w $fname -a -x $fname]
then
	echo "have all permission"
else
	echo "no permission"
fi
else
	echo "file not exists"
	fi
	
