import re

#data = 'welcome to surat'
data = 'welcome to SURAT'
pattern = '[aeiou]'
#pattern = '[aeiouAEIOU]'

#rst = re.search(pattern,data)
#rst = re.split(pattern,data)
rst = re.split(pattern,data,flags = re.I)
print(rst)