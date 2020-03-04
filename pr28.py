f1 = open("FIRST3.txt", "r+")
line = 0
word = 0
char = 0
for i in f1.read():
    if i is not None:
        char += 1
    if i == " " or i == '.':
        word += 1
        if i == '.':
            line += 1

print('line =', line)
print('word =', word)
print('char =', char)

f1.close()