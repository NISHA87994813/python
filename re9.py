import re

text_phrase = 'This is a String!. But it has a punctuation. How can we remove it?'
#rst = re.findall(r'[^!.? ]+',text_phrase)
#print(rst)
pattern = '[!.? ]'
rst = re.split(pattern,text_phrase)
print(rst)
