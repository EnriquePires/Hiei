Program = 'On'

def check_from_n(lowest = 3, stop_at = 10000000, jump = 2): #Finds if there are two consecutive primes (difference = 2) bigger than the lowest number. The stop_at is to set up a limit but it can be increased if non primes were found. Then it does a jump
	mini = max(int(lowest),3)
	total = max(int(stop_at),3)
	maxi = mini+total

	Primes = [True]*maxi
	Primes[0] =False #0 is not a prime
	Primes[1] = False #1 is not a prime
	par_sweep = 4
	while par_sweep < maxi:
		Primes[par_sweep] == False
		par_sweep += 2
	p = 3
	while p+2 < maxi:
		if Primes[p]:
			if ((Primes[p+2]) and (p >= mini)):
				print('Primes found!\n',str(p),'\n',str(p+2),'\n')
				return([p,p+2])
			x = int(maxi/p) - int(maxi%p == 0)
			while x >= p:
				if Primes[x]:
					Primes[x*p] = False
				x -= 1
		p += 2
	l = stop_at*jump
	while True:
		print('We cover the maximum value to consider. Do you want to test with ', str(l), ' as a maximum vale?')
		inp = input ('(Y/N) :')
		if inp == 'N':
			print('Thank you for using this program, have a good day!')
			return([0,mini+4])
		if inp == 'Y':
			return(check_from_n(lowest, l, jump))
		else:
			print('Valid options are Y and N. Lets try again ') 







while Program == 'On':
	stop = False
	a = input('select a Lower_bond for your prime: ')
	while True:
		while True:
			b = input('do you want a standard configuration (Y/N)? :')
			if b == 'Y':
				result = check_from_n(lowest = a)
				break
			if b == 'N':
				print('please select your configuration')
				maxim = input('what is the total of numbers you want to search? The higher the number the slower the process will be :')
				product = input('pick a number to multiply the maximim with if the process fails :')
				result = check_from_n(a,int(maxim),float(product))
				break
			else:
				print('please, select between Y and N')
		while ((int(a) < result[1]) and (not stop) and (result[0] != 0)):
			c = input('Do you want to find another prime (Y/N)? :')
			if c == 'N':
				print('Thank you for using this application!')
				Program = 'Off'
				break
			if c == 'Y':
				while True:
					next = input('do you want to find the next consecutive pair (Y/N)?')
					if next == 'Y':
						a = result[1]
						break
					if next == 'N':
						stop = True
						break
					else:
						print('please, select between Y and N')
			else:
				print('please, select between Y and N')
		if result[0] == 0:
			Program = 'Off'
		if int(a) < result[1]:
			break


