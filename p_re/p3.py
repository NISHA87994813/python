import re

p = '<.*?>'
text = '<python>perl>'

lst = re.findall(p,text)
print(lst)