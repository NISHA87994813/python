'''greedy and non-greedy matching
	<.*>	: Greedy repetition : matches <python>perl>
	<.*?>  	: non-greedy repetition : matches <python> in <python>perl>
'''
import re	

tx = '<python>perl>'
#p = r'<.*>'
p = r'<.*?>'

print(re.findall(p,tx))