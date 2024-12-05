import re

phrase = "test phrase match is in match middle"

#a = re.findall('match',phrase)
a = re.findall('match',phrase,re.I)
print(a)
print(type(a)) 