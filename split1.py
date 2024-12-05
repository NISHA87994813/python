import re
data = "welcome to surat"
#splitter = ' '
#splitter = 'o'
splitter = '.'
#help(re.split)
rst = re.split(splitter,data)
print(rst)