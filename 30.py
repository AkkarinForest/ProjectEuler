limit = 354294
result = 0
for i in range(2,limit+1):
	j = str(i)
	sum = 0
	for x in j:
		y = int(x)
		sum += y**5
	if sum == i:
		result += sum
		print sum

print result
		



