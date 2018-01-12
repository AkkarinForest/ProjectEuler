from time import time
start = time()

perfect = []

for i in range(100):
	perfect.append(i*i)	

print perfect

for x in xrange(1,5000):
	print x
	for y in xrange(1,x):
		for z in xrange(1,y):
			if all(i in perfect for i in [x+y, x-y, x+z, x-z, y+z, y-z]):
				print "hura", x, y, z, x+y+z

print(time() - start)



