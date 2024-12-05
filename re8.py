import re

def multi_re_find(patterns,text_phrase):
	for pattern in patterns:
		print("seraching for pattern %r"%(pattern))
		print(re.findall(pattern,text_phrase))
		print()


text_phrase = 'sdsd..sssddd..sdddsddd..dsds..dsssss..sdddd'

text_patterns = ['[sd]',#either s or d
				's[sd]',# ss or sd
				's[sd]+']#s followed by one or more s or d
				
multi_re_find(text_patterns,text_phrase)
