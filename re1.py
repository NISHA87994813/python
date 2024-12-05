import re

patterns = ['term','term2']

text = "welcome to python programming in this term we will start re..."
for pattern in patterns:
	if(re.search(pattern,text)):
		print("found")
	else:
		print("not found")
	