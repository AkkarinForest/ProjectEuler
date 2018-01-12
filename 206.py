from math import sqrt

down = int(sqrt(10203040506070809))
up =   int(sqrt(19293949596979899))+1
print(down, up)
for i in xrange(down,up,2):
	digits=""
	number = i*i
	digits = str(number)[::2]
	print(i)
	if digits == "123456789":
		print("final",i, number)
		break
				
	





