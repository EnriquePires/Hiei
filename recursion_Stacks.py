from Stack import Stack

from os.path import join
def move(n,f, t, v1,v2,v3):
	if n == 0:
		print('ok?')
	elif n == 1:
		if f == 1 and t == 2:
			v1.transfer(v2)
		if f == 1 and t == 3:
			v1.transfer(v3)
		if f == 2 and t == 3:
			v2.transfer(v3)

		if f == 2 and t == 1:
			v2.transfer(v1)
		if f == 3 and t == 1:
			v3.transfer(v1)
		if f == 3 and t == 2:
			v3.transfer(v2)
		

	else:
		if f == 1 and t == 2:
			move(n-1,1,3,v1,v2,v3)
			move(1,1,2,v1,v2,v3)
			move(n-1, 3,2,v1,v2,v3)
		if f == 1 and t == 3:
			move(n-1,1,2,v1,v2,v3)
			move(1,1,3,v1,v2,v3)
			move(n-1, 2,3,v1,v2,v3)
		if f == 2 and t == 3:
			move(n-1,2,1,v1,v2,v3)
			move(1,2,3,v1,v2,v3)
			move(n-1, 1,3,v1,v2,v3)
		if f == 2 and t == 1:
			move(n-1,2,3,v1,v2,v3)
			move(1,2,1,v1,v2,v3)
			move(n-1, 3,1,v1,v2,v3)
		if f == 3 and t == 1:
			move(n-1,3,2,v1,v2,v3)
			move(1,3,1,v1,v2,v3)
			move(n-1, 2,1,v1,v2,v3)
		if f == 3 and t == 2:
			move(n-1,3,1,v1,v2,v3)
			move(1,3,2,v1,v2,v3)
			move(n-1, 1,2,v1,v2,v3)




def stack_pass(n):
	v1 = Stack('v1')
	v2 = Stack('v2')
	v3 = Stack('v3')
	for i in range(n):
		v1.add(n-i)
	print('')
	print('lets move a stakc of' + ' ' + str(20) + ' ' + 'numbers ordered descendently to another stack using a third stack.')
	move(n, 1,2,v1,v2,v3)



stack_pass(5)

# reported_move(25,1,3,list(range(25)),[],[])

# THE ABOVE ONE WILL TAKE MORE THAN ONE HOUR!!!


