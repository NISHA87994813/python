import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

#we can capture things with paranthesis,then refer to the captured items by \1,\2.. 
#in the substitution
			   
#tx = re.sub(r'(\w*)o(\w*)',r'=\1o\2=',tx)
#print(tx)

#we can also assign names to the captured things
tx = re.sub(r'(?P<before>\w*)o(?P<after>\w*)',r'=\g<before>o\g<after>=',tx)
print(tx)

#we can make pattern, but apparently not the substitution. clearly by adding ?x and whitespaces

#tx = re.sub(r'(?x) (?P<before> \w*) o (?P<after> \w*)',r'=\g<before>o\g<after>=',tx)
#print(tx)

#easire format

#tx = re.sub(r'(?x) (\w*o\w*)',r'=\1=',tx)
#print(tx)
