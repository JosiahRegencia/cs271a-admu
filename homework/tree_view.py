class TreeView:
	def __init__(self):
		self.zero = list()
		self.one = list()
		self.two = list()
		self.three = list()
		self.four = list()
		self.five = list()

	def add_node(self, level):
		if level == 0:
			self.zero.append(level)
		elif level == 1:
			self.one.append(level)
		elif level == 2:
			self.one.append(level)
		elif level == 3:
			self.one.append(level)
		elif level == 4:
			self.one.append(level)
		elif level == 5:
			self.one.append(level)

	def print_tree(self):
		for i in range(121):
			while i != 120:
				print(" ", end=" ")
			print(self.zero[0])

		for i in range(123):
			while i != 120:
				print(" ", end=" ")
			for j in self.one:
				print(j, end=" ")

		for i in range(126):
			while i != 117:
				print(" ", end=" ")
			for j in self.two:
				print(j, end=" ")

		for i in range(135):
			while i != 108:
				print(" ", end=" ")
			for j in self.three:
				print(j, end=" ")

		for i in range(162):
			while i != 81:
				print(" ", end=" ")
			for j in self.four:
				print(j, end=" ")

		for i in range(243):
			while i != 0:
				print(" ", end=" ")
			for j in self.five:
				print(j, end=" ")
