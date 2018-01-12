def updatepose(pose):

	pose[-1] += 1
	
	print pose
	yield pose
	if pose[-1] > pose[-2]:
		pose[-1] -= 1
		pose[-2] += 1
	print pose #00010
	yield pose		

	for i in range(3):
		pose[-1] += 1
		print pose
		yield pose
		
		if pose[-1] > pose[-2]:
			if pose[-2] > pose[-3]:
				if pose[-3] > pose[-4]:
					pass
				pose[-2] -= 1
				pose[-3] += 1
				print pose
				yield pose
			else:
				pose[-1] -= 1
				pose[-2] += 1
				print pose
				yield pose
		
	return 


pyramid = [['1'], ['1', '2'], ['1', '2', '3'], ['1', '2', '3', '4'], ['1', '2', '3', '4', '5']]

position = [0,0,0,0,0]

y = updatepose(position)
biggest = 0

while position != [0,0,1,2,3]:
	x = 0
	for i in range(len(pyramid)):
		x += int(pyramid[i][position[i]])
	if x > biggest: biggest = x
	print x
	position = next(y)


print biggest







