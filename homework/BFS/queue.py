class Queue:
	def __init__(self):
		self.queue = list()

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		try:
			front = front()
			self.queue.remove(front)
		except IndexError as error:
			print 'Error: ', error
			print 'Queue is empty'

	def front(self):
		try:
			return self.queue[0]
		except IndexError as error:
			print 'Error: ', error
			print 'Queue is empty'

	def rear(self):
		try:
			return self.queue[len(self.queue) - 1]
		except IndexError as error:
			print 'Error: ', error
			print 'Queue is empty'