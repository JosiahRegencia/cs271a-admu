class Stack:
	def __init__(self):
		self.stack = list()

	def is_empty(self):
		if len(self.stack) == 0:
			return True
		return False

	def top(self):
		try:
			return self.stack[len(self.stack) - 1]
		except IndexError as error:
			print 'Error: ', error
			print 'Stack is empty'

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		try:
			top = self.top()
			self.stack.remove(top)
			return top
		except ValueError as error:
			print 'Error: ', error
			print 'Stack is empty'