result = 0

for i in range(999,99,-1):
	for j in range(999,99,-1):
		number = str(i*j)
		if len(number)%2==0:
			print(number[(len(number)/2)-1::-1],number)
			if number[(len(number)/2-1)::-1]==number[(len(number)/2):]:
				if result < int(number):
					result = int(number)		
		#else:	
		#	if number[len(number)/2-1::-1]==number[(len(number)/2+1):]:
		#		if result < int(number):
		#			result = number		
			
print result



