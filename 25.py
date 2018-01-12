#from math import log10
numbers = [1,2]
#x = int(log10(numbers[-1]))+1
x = 1
while x<1000:
#	print(numebr)
	numbers.append(numbers[-2]+numbers[-1])
	x = len(str(numbers[-1]))
print numbers[-1], "index ", len(numbers)+1 
	 
