

import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

#lst = re.split(r'(?x) o',tx)
lst = re.split(r'(?x) (o)',tx)

print(lst)


