"""
	Please refer to queue.py, stack.py, and node.py also.
"""


from node import Node 
from stack import Stack
from queue import Queue

import sys


def BFS(tree, depth_level):
	while not tree.is_empty():
		front = tree.dequeue()
		if front.level > depth_level:
			""" 
				This is the level tracker
				refer to node.py for creation of children
				also, in node.py every creation already increments the level by 1
				The code stops once it reaches a node in level 6, hence, break command
			 """
			break

		print 'node: {}\tis_goal: {}\tnode level: {}' .format(front, front.is_goal, front.level)

		if not front.is_goal:
			children = front.create_children(3)
			for child in children:
				tree.enqueue(child)

		elif front.is_goal:
			break

def DFS(tree, depth_level):
	while not tree.is_empty():
		top = tree.pop()

		print 'node: {}\tis_goal: {}\tnode level: {}' .format(top, top.is_goal, top.level)

		if not top.is_goal:
			if top.level == depth_level:
				""" 
					This is the level tracker
					refer to node.py for creation of children
					also, in node.py every creation already increments the level by 1
					Used continue since it has to go back to parent nodes and dig deep from there
				"""
				continue
			else:
				children = top.create_children(3)
				for child in children[::-1]:
					"""
						Looped starting from the last index so that 
						the traversal will start digging on the left
						instead of the right
					"""
					tree.push(child)

		elif top.is_goal:
			break

def main():
	commands = ['bfs', 'dfs']
	root = Node(0)

	try:
		traversal = sys.argv[1].lower()
		if traversal == commands[0]:
			tree = Queue()
			tree.enqueue(root)
			BFS(tree, 5)
		elif traversal == commands[1]:
			tree = Stack()
			tree.push(root)
			DFS(tree, 5)
		else:
			print 'Only \'BFS\' or \'DFS\' allowed arguments'
	except IndexError as error:
		print' Error: ', error
		print 'Must pass \'BFS\' or \'DFS\' as argument'


if __name__ == '__main__':
	main()