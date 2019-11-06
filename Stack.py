

class Stack():
	def __init__(self, name = ''):
		self.name = name
		self.top = -1
		self.mark = []
	def add(self,x): #ADD ONE ELEMENT AT THE TOP OF THE STACK
		self.top += 1
		self.mark.append(x)
	def pop(self): # REMOVE TOP ELEMENT FROM THE STACK
		if self.top > 0:
			self.mark = self.mark[0:self.top]
			self.top -= 1
		else:
			if self.top == 0:
				self.top = -1
				self.mark = []
			else:
				print('')
				print('ERROR WHILE TRYING TO POP. THERE IS NOTHING TO POP')
	def point(self): # SHOW THE VALUE OF THE TOP OF THE STACK
		return self.mark[self.top]

	def transfer(self, receiver): # SEND TOP ELEMENT FROM ONE STACK TO ANOTHER, PLACING IT ON THE TOP OF THE RECEIVER STACK
		if self.top == -1:
			print('')
			print('ERROR WHILE TRYING TO POP. THERE IS NOTHING TO POP')
		else:
			receiver.add(self.point())
			self.pop()
			print('')
			print(str(receiver.point()) + ' transfered from ' + self.name + ' to ' + receiver.name)
			print('')
			print(self.name + ' is now ')
			print(self.mark)
			print('')
			print(receiver.name + ' is now ')
			print(receiver.mark)
			print('')

	def attach(self, transfer_stack): # TRANSFER ALL ELEMENTS FROM ONE TRANSFER STACK TO ANOTHER STACK
		while transfer_stack.top != -1:
			transfer_stack.transfer(self)
		return self

	def dive(self,receiver_stack): # BASICALLY THE CONTRARY OF ATTACH
		return receiver_stack.attach(self)

	def reverse(self): # Creates a stack called equal to your original stack with the elements of your stacked flipped face down. WARNING this method empties your stack
		return self.dive(generate_stack(string_name = self.name))


def generate_stack(list = [], string_name = 'Unnamed stack'):
	z = Stack(string_name)
	for x in list:
		z.add(x)
	return z




			

