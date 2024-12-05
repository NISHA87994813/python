import re

pattern = 'TerM'
#pattern = 'TerM1'

#text = "welcome to python programming in this term we will start re..."
text = "welcome to python programming in this term we will start re...terM"

#rst = re.search(pattern,text,re.IGNORECASE)
rst = re.search(pattern,text,re.I)
		
print(rst)
print(type(rst))

print(rst.start())
print(rst.end())
