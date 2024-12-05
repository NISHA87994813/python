import re

test = "All cats are smarter than dogs"

'''
#p = '.'
#p = '..'
#p = r'.'
p = r'.*'
matchobj = re.match(p,test)
#matchobj = re.match(p,test,re.I)
print(matchobj)
print(matchobj.group())
'''

#matchobj = re.match((r'(.*) are (.*?) .*'),test,re.I)
#matchobj = re.match((r'(.*) are (.*?) (.*)'),test,re.I)
#matchobj = re.match((r'(.*) are (.*)'),test,re.I)
matchobj = re.match((r'(.*) are (.*?)'),test,re.I)

#if matchobj != None:
if matchobj:
	print("found")
	print(matchobj.group())
	print(matchobj.group(1))
	print(matchobj.group(2))
	print(matchobj.group(3))
	#print(matchobj.group(4))
else:
	print("not found")
