import re

tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."
#p = r'(\w*)o(\w*)'
#r = r'=\1o\2='
p = r'(?P<a>\w*)o(?P<b>\w*)'
r = r'=\g<a>o\g<b>='

#t1 = re.findall(p,tx)
t1 = re.sub(p,r,tx)

print(t1)

