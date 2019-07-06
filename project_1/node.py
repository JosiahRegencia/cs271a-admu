import random


class Node:
	def __init__(self, level, current):
		self.current = current
		self.level = level
		self.children = list()

	def is_goal(self, Knight, Enemy):
		if Knight.location != Enemy.location:
			return False
		return True

	def create_children(self,Knight):
		move_list = Knight.possible_moves(self.level,self.current)
		temp = Knight.location
		for i in range(0, len(move_list)):
			new_level = temp[0] + move_list[i][0]
			new_current = temp[1] + move_list[i][1]
			self.children.append(Node(new_level,new_current))
		return self.children
