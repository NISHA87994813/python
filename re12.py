import re

phone = '2004-342-212 # this is a phone number'

num = re.sub(r'#.*$',"",phone)
print("Phone num : ",num)

num = re.sub(r'\D',"",phone)
print("Phone num : ",num)