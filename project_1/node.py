import random


class Node:
	def __init__(self, parent, level, current):
		self.parent = parent
		self.grand_parent = None
		self.current = current
		self.level = level
		self.children = list()

		if parent != None and parent.parent != None:
			self.grand_parent = parent.parent

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
			print ('Node: ', self)
			if self.parent == None:
				self.children.append(Node(self, new_level, new_current))
				print ('(x, y): ', (new_level, new_current))
			else:
				print ('' + str((self.parent.level, self.parent.current)) + '=' + str((new_level, new_current)))
				if (self.parent.level, self.parent.current) != (new_level, new_current):
					print ('(x, y): ', (new_level, new_current))
					self.children.append(Node(self, new_level,new_current))
		print ('\n')
		return self.children
