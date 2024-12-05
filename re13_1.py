import re

tx = 'abcd...aabcd...aba...'

#pattern = '(ab)'
#pattern = '(ab*)'
#pattern = '(ab)*'
#pattern = '(ab)+'
pattern = '(ab)?'

print(re.findall(pattern,tx))