mainstr=input('Enter main string : ')
sub=input('Enter sub string : ')
N=int(input('Enter the position where you want to insert : '))
print("The original string : " +mainstr)
print("The add string : " +sub)

finalstr = list(mainstr)
finalstr.insert(N,sub)
finalstr = ''.join(finalstr)

# print finalstrult
print("The final string after performing addition : " + str(finalstr))