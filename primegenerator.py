def check_from_n(termination = 0, n = 5000, powerjump = 1, productjump = 2): #Finds if there is a number with the termination given in the first n numbers. Then it does a jump
	ter = int(termination)
	if ter == 0:
		print('\nThis is not a valid termination. We will assume that you want any prime\n')
		print(2)
		return(2)
	if ter < 0:
		print('\nWe cant work with negative numbers, we will take the absolute value of this termination')
		ter = (-1)*ter

	if ter in [2,5]:
		print('\nPrime found!\n')
		print(ter)
		return(ter)
	if (x%2 == 0 or x%5 ==0):
		print('\nWe cant find a prime with this termination because it is a multiple of 2 or 5, thus any number with this termination will have the similar property and hence it wont be a prime. Sorry\n')
		return()

	Primes = [True]*n
	Primes[0] =False #0 is not a prime
	Primes[1] = False #1 is not a prime
	p = 2
	s = 1 #Salto
	lst = len(str(termination))
	y = 0
	while p < n:
		if Primes[p]:
			if int(str(p)[len(str(p))-lst:len(str(p))]) == termination: #We check if the prime ends with the termination we want
				print('\nPrime found!\n')
				print(p)
				return(p)
			x = int(n/p)- int(n%p == 0)
			while True:
				if Primes[x]:
					Primes[x*p] = False
					if x == p:
						break
				x -= 1
		p += s
		s = 2
	l = (n**powerjump)*productjump
	while True:
		inp = input('\nWe cover the maximum value to consider. Do you want to test with ', str(l), ' as a maximum vale (Y/N)?: ')
		if inp == 'N':
			print('\nThank you for using this prime generator, have a good day!')
			return()
		if inp == 'Y':
			return(check_from_n(ter, l, powerjump, productjump))
		else:
			print('\nValid options are Y and N. Lets try again ')











x = int(input('select a termination for the prime: '))
if x == 0:
	print('\nThis is not a valid termination. We will assume that you want any prime\n')
	y = 2
if x < 0:
	print('\nWe cant work with negative numbers, we will take the absolute value of this termination')
	x = (-1)*x
if x in [2,5]:
	print('\nPrime found!\n')
	y = x
else:
	if (x%2 == 0 or x%5 ==0):
		print('\nWe cant find a prime with this termination because it is a multiple of 2 or 5, thus any number with this termination will have the similar property and hence it wont be a prime. Sorry\n')
		y = 'Not Found'






