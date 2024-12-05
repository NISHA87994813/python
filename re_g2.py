#greedy and lazy matching

import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

p = r'(?x) (o) (.*) \1'
#greedy matching
fi = re.findall(p,tx)

print(fi)


#lazy matching
p1 = r'(?x) (o) (.*?) \1'
fi = re.findall(p1,tx)

print(fi)


