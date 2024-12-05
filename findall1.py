import re
data = "welcome to surat"
#splitter = ' '
#splitter = 'o'
splitter = '.'
#help(re.findall)
rst = re.findall(splitter,data)
print(rst)