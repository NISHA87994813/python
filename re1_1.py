import re

patterns = ['term','term1']

text = "in this term we will learn re in python"

for pattern in patterns:
	rst = re.search(pattern,text)
	if(rst):
		print("Found")
	else:
		print("not Found")
