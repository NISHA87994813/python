import re

pattern = 'term'
#pattern = 'terM'

text = "in this term we will learn re in python"

rst = re.search(pattern,text)
print(rst)
print(type(rst))
print(rst.start())
print(rst.end())