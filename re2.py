import re
patterns = ['TerM','term2']

text = "welcome to python programming in this term we will start re..."
for pattern in patterns:
	if(re.search(pattern,text,re.IGNORECASE)):	# re.I
	#if(re.search(pattern,text,re.IGNORECASE)!=None):	
		print("found")
	else:
		print("not found")
	