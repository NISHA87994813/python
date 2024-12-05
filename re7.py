import re

def multi_re_find(patterns,text_phrase):
	for pattern in patterns:
		print("seraching for pattern %r"%(pattern))
		print(re.findall(pattern,text_phrase))
		print()


text_phrase = 'sdsd..sssddd..sddssdd..sdddsddd..dsds..dsssss..sdddd'

text_patterns = ['sd*','[sd]*','(sd)*',
				'sd+',
				'sd?',
				'sd{3}',
				'sd{1,3}',				
				'sd{2,}',	
				'sd{,2}'				
				]
				
multi_re_find(text_patterns,text_phrase)