print('')
print('hello ZA WARUDO!')
print('')
print('TOKI WO TOMARE')
print('')

from Stack import Stack
print('succesfull import')
print( ' --- space --- ')
print(' you are so succcesssfulll')


def sreverse(string):
	tempstack = Stack()
	while string != '':
		l = len(string)
		tempstack.add(string[0])
		string = string[1:l]
		#print(tempstack.top)
		#print(tempstack.mark)
		#print(string)
	while tempstack.top != -1:
		#print(string)
		#print(tempstack.top)
		#print(tempstack.mark)
		string += tempstack.point()
		tempstack.pop()
	return string

def lreverse(lista):
	tempstack = Stack()
	while lista != []:
		l = len(lista)
		tempstack.add(lista[0])
		lista = lista[1:l]
	while tempstack.top != -1:
		lista.append(tempstack.point())
		tempstack.pop()
	return lista

# ----------------------------------------------------------- PREFIX AND POSTFIX ------------------------------------------------------------------------------------------

def expression(string):
	Operators = ['*', '+', '-', '/']
	def operation(x,y,operator):
		j = 0
		if operator == '+':
			return x + y
		elif operator == '*':
			return x * y
		elif operator == '-':
			return x - y
		elif operator == '/':
			return x / y
		else:
			print('ERROR. operator not introduced correctly')
				



	def lastterm(x):
		if x[-1] not in Operators:
			x[-1] = jump
			x.pop()
			return jump
		else:		
			stack = Stack()
			while x[-1] in Operators:
				stack.add(x[-1])
				x.pop()
			while stack.top != -1:
				a = x[-1]
				x.pop()
				op = stack.point()
				stack.pop()
				b = lastterm(x)
				x.append(operation(a,b,op))















sreverse('holaaa')

























# -----------------------------------------------------------------REVERSE LINKED LISTS ---------------------------------------------------------------------------------------------------------------------------------------------	


class LinkedList(object):
	def __init__(self,nodes):
		#self.dict = dict()
		#self.pointer_head = pointer_head
		self.nodes = nodes
		self.dict = dict()
		self.start = nodes[0]
		try:
			for i in range(1,len(nodes)):
				self.dict[nodes[i-1]] = nodes[i]
		except:
			pass

	def select(self, n):
		x = self.start
		i = 0
		while i < n:
			x = self.dict[x]
			i += 1
		return x

	def select_end(self):
		x = self.start
		while True:
			try:
				x = self.dict[x]
			except:
				break
		return x
		

	def insert_end(self, node):
		self.dict[LinkedList.select_end(self)] = node

	def insert_start(self, node):
		self.dict[node] = self.start
		self.start = node

	

	def insert(self, node,n):

		if n == 0:
			LinkedList.insert_start(self, node)
		else:
			x = LinkedList.select(self,n-1)
			y = self.dict[x]
			self.dict[x] = node
			self.dict[node] = y

	def previous(self, node):
		x = self.start
		while self.dict[x] != node:
			x = self.dict[x]
		return(x)

		
	def remove_node(self, node):
		if node != self.start:
			try:
				post = self.dict[node]
				self.dict[LinkedList.previous(self, node)] = post
			finally:
				self.dict.pop(node,None)
		else:
			try:
				self.start = self.dict[node]
			finally:
				del self.dict[node]

	def remove(self,n):
		LinkedList.remove_node(self, LinkedList.select(self,n))

	def reverse(self):
		def rev(node):
			try:
				check = self.dict[self.dict[node]]
				rev(self.dict[node])
			except:
				self.start = self.dict[node]

			self.dict[self.dict[node]] = node
			self.dict.pop(node,None)

		rev(self.start)


	def printrec(self):
		def printfoll(node):
			print('')
			print('Node Value = ', node.value)
			print('Node Address = ', node.address)
			try:
				printfoll(self.dict[node])
			except:
				print('Not Linked')

		printfoll(self.start)

	def revprint(self):
		def printback(node):
			try:
				printback(self.dict[node])

			except:
				pass

				
			print('')
			print('Node Value = ', node.value)
			print('Node Address = ', node.address)

		printback(self.start)


