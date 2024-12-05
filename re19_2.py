# but we dont want to consume 'born'

import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

#lst = re.split(r'(?x) \b (?!born) \w{4} \b',tx)
#lst = re.split(r'(?x) \b \w{4} (?!born) \b',tx)
lst = re.split(r'(?x) \b \w{4} (?<!born)\b',tx)

print(lst)


