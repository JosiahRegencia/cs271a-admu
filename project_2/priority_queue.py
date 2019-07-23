import heapq

class Priority_queue:
    def __init__(self):
        self.queue = list()

	def is_empty(self):
		if len(self.queue) == 0:
			return True
		return False

    def sort(self):
        heapq.heapify(self.queue)

	def front(self):
		try:
			return self.queue[0]
		except IndexError as error:
			print ('Error: ', error)
			print ('Queue is empty')

    def rear(self):
        try:
            return self.queue[len(self.queue) - 1]
        except IndexError as error:
            print ('Error: ', error)
            print ('Queue is empty')

    def enqueue(self, item):
		self.queue.append(item)

    def dequeue(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].distance_to_goal < self.queue[min].distance_to_goal:
                    min = i
            out = self.queue[min]
            del self.queue[min]
            return out
        except IndexError as error:
            print('Error: ', error)
            print('Queue is empty')
