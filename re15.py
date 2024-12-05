import re	

tx = 'ruby,Ruby,RUby,RUBY'
p = 'R(?i)uby'
#p = 'R(?i:uby)'
#p = 'Ruby'
#p = 'R(?i:u)by'

print(re.findall(p,tx))