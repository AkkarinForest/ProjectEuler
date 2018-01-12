roots = 0
sumy = 0

for i in range(101):
	roots += i*i
	
print(sum(range(101))**2 - roots)


