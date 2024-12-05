import re

def multi_re_find(patterns,text_phrase):
	for pattern in patterns:
		print("seraching for pattern %r"%(pattern))
		print(re.findall(pattern,text_phrase))
		print()

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag.'

test_patterns = [
			r'\d+',		#seq of digits
			r'\D+',		#seq of non-digits
			r'\s+',		#seq of whitespaces
			r'\S+',		#seq of non-whitespaces
			r'\w+',		#alphanumeric characters
			r'\W+'		#non-alphanumeric
			]
			
multi_re_find(test_patterns,test_phrase)			