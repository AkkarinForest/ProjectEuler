from math import sqrt
from time import time

start = time()
aband = []
for j in range(12,28123):
	sum=1
	for i in range(2,int(sqrt(j))+1):
		if j%i==0:
			if i!=j/i:
				sum = sum + i + j/i
			else:
				sum = sum + i
	if sum > j:
		aband.append(j)

#print(aband)

"""result = 0

for i in range(1,28124):
	toadd = 1
	j = 0
	while aband[j] < i:
		k = i - aband[j]
		j = j + 1
		if k in aband[j:]:
			toadd = 0
			break
	if toadd == 1:
		result = result + i
		print(result)
print(result)
"""

possible = set()
for a in aband:
	for b in aband:
		if a + b < 28123: possible.add(a+b)
		else:
			break

#print(possible)

result = 0

for i in range(28123):
	if i not in possible:
		result += i

print(result)




end = time() - start
print("time", end)












