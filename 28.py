sum = 1
last = 1
for i in range(2,1001,2):
	for j in range(4):
		sum = sum + last + i
		last = last + i

print (sum)
