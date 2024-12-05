
import re

def multi_re_find(patterns,text_phrase):
	for pattern in patterns:
		print("seraching for pattern %r"%(pattern))
		print(re.findall(pattern,text_phrase))
		print()

test_phrase = 'THis is an example sentence. Lets see if we find some letters.'

test_patterns = [
			'[a-z]+',		#seq of lowercase letters
			'[A-Z]+',		#seq of uppercase letters
			'[a-zA-Z]+', 	#seq of lowercase or uppercase letters
			'[A-Z][a-z]+',	#1 uppercase followed by lowercase letters
			'[A-Z]+[a-z]+',	#1-n uppercase followed by lowercase letters
			'[0-9]+'		#for digits
			]
			
multi_re_find(test_patterns,test_phrase)			