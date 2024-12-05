import re

split_term = '@'
#phrase = "what is the domain name of someone with email : 'a@gmail.com'"
phrase = "what is the domain name of someone with email : 'a@gmail.com and b@gmail.com'"

a = re.split(split_term,phrase)
print(a)
print(type(a))