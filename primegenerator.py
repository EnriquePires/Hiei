def check_from_n(termination = 0, n = 10000000, powerjump = 1, productjump = 2): #Finds if there is a number with the termination given in the first n numbers. Then it does a jump
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
	if (ter%2 == 0 or ter%5 ==0):
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
			if (int(str(p)[len(str(p))-lst:len(str(p))]) == ter): #We check if the prime ends with the termination we want
				print('\nPrime found!\n')
				print(p)
				return(p)
			x = int(n/p)- int(n%p == 0)
			while x >= p:
				if Primes[x]:
					Primes[x*p] = False
				x -= 1
		p += s
		s = 2
	l = (n**powerjump)*productjump
	while True:
		print('We cover the maximum value to consider. Do you want to test with ', str(l), ' as a maximum vale?')
		inp = input ('(Y/N) :')
		if inp == 'N':
			print('Thank you for using this prime generator, have a good day!')
			return()
		if inp == 'Y':
			return(check_from_n(ter, l, powerjump, productjump))
		else:
			print('Valid options are Y and N. Lets try again ')


Program = 'On'
while Program == 'On':
	a = input('select a termination for your prime: ')
	while True:
		b = input('do you want a standard configuration (Y/N)? :')
		if b == 'Y':
			check_from_n(termination = a)
			break
		if b == 'N':
			print('please select your configuration')
			maxim = input('what is the maximum value you want to search? The higher the number the slower the process will be :')
			power = input('now pick how much you want to elevate the maximum if the process doesnt find any preime. Pick a low number :')
			product = input('pick a number to multiply the maximim with if the process fails :')
			check_from_n(a,int(maxim),float(power),float(product))
			break
		else:
			print('please, select between Y and N')
	while True:
		c = input('Do you want to find another prime (Y/N)? :')
		if c == 'Y':
			break
		if c == 'N':
			print('thank you for using this aplication')
			Program = 'Off'
			break
		else:
			print('please, select between Y and N')















