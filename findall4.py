import re
#data = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa"
data = "a aa aaa aabaa aaaaba aabaaaa abaaaaaa"

splitter = 'a?'

rst = re.findall(splitter,data)
print(rst)