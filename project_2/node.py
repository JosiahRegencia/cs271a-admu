import random
from heuristic import cell
from heuristic import heuristic

class Node:
	# heuristic
	def __init__(self, parent, level, current, heuristic):
	# def __init__(self, parent, level, current):
		self.parent = parent
		self.current = current
		self.level = level
		self.children = list()
		self.distance_to_goal = heuristic

		if parent != None and parent.parent != None:
			self.grand_parent = parent.parent

	def is_goal(self, Knight, Enemy):
		if Knight.location[0] == Enemy.location[0]:
			if Knight.location[1] == Enemy.location[1]:
				return True
			return False
		return False

	def create_children(self,Knight, Enemy):
		move_list = Knight.possible_moves(self.level,self.current)
		temp = Knight.location
		for i in range(0, len(move_list)):
			new_level = temp[0] + move_list[i][0]
			new_current = temp[1] + move_list[i][1]
			if self.parent == None:
				self.children.append(Node(self, new_level, new_current, heuristic((new_level,new_current),Enemy.location,3)))
			else:
				if (self.parent.level, self.parent.current) != (new_level, new_current):
					self.children.append(Node(self, new_level,new_current,heuristic((new_level,new_current),Enemy.location,3)))

		print('Number of possible moves: {}'.format(len(self.children))),
		print('\t'),
		print ('Possible moves: '),
		for child in self.children:
			print('({},{})'.format(child.level, child.current)),
			print('\t'),
		print ('\n')
		return self.children
