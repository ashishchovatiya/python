keys = [11,12,13,14]
values = ['ashish','pranav','raj','dharm']

print ("Key list is : " + str(keys))
print ("Value list is : " + str(values))
res = {}
for i in range(len(keys)):
		res[keys[i]] = values[i]
print ("Dictionary is : " + str(res))
