#greedy and lazy matching

import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

#greedy matching
#fi = re.finditer(r'(?x) / (.*) /',tx)
fi = re.findall(r'(?x) / (.*) /',tx)

print(fi)

#lazy matching
#fi = re.finditer(r'(?x) / (.*) /',tx)
fi = re.findall(r'(?x) / (.*?) /',tx)

print(fi)

