#capturing in the pattern for split
import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

try:
	lst = re.split(r'\b',tx)
	print(lst)
except ValueError as e:
	print(e)