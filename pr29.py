import re

k = []
text = "ahh shit, here we go again"
l = re.split(" ", text)
for p in l:
    if re.match('[a][a-z]*', p):
        k.append(p)
print(k)