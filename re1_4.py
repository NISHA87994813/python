import re

#pattern = 'term'
pattern = 'terM'

text = "in this teRm we will learn re in python . term and term"

#rst = re.search(pattern,text,re.IGNORECASE)
rst = re.search(pattern,text,re.I)
print(rst)
print(type(rst))
