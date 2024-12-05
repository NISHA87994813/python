import re	

tx = 'this is Python! lang.and we are working on Python! Python'

#p = 'Python!' #will return ['Python!','Python!']
#p = 'Python(?=!)'	# Python(?=re)
p = 'Python(?!!)'

print(re.findall(p,tx))