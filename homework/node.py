import random


class Node:
	def __init__(self, level):
		self.level = level
		self.children = list()
		self.is_goal = self.is_goal()

	def is_goal(self):
		basis = random.randint(1, 21)
		if basis != 8:
			return False
		return True

	def create_children(self, length=1):
		for i in range(0, length):
			self.children.append(Node(self.level+1))
		return self.children
