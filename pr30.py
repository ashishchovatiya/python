import re

text = 'ahh shit, here we go again'
x = re.findall("[a-z]+$", text)
print(x)