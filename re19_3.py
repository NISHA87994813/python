import re
tx = "the quick brown fox born on 1/23/2013 jumped over the lazy dog born on 10/6/10."

lst = re.split(r'(?x) \b (?!\w*o) \w{4} \b',tx)

print(lst)


