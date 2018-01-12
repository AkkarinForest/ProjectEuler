def fibo(a,b, sum):
	if a+b>4000000:
		print(sum)
		
		return numbers
	numbers.append(a+b)
	if (a+b)%2==0:
		sum = sum + a+b
	fibo(b, a+b, sum)	

numbers = [1,2]
sum = 2
fibo(1,2,sum)
