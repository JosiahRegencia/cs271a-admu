"""
	Please refer to queue.py, stack.py, and node.py also.
"""


from node import Node 
from stack import Stack
from queue import Queue


def BFS(tree):
	while not tree.is_empty():
		front = tree.dequeue()

		print 'node: ', front
		print 'is_goal: ', front.is_goal
		print 'node level: ', front.level
		print '\n'
		
		if front.level > 5:
			""" 
				This is the level tracker
				refer to node.py for creation of children
				also, in node.py every creation already increments the level by 1
				The code stops once it reaches a node in level 6, hence, break command
			 """
			break

		if not front.is_goal:
			children = front.create_children(3)
			for child in children:
				tree.enqueue(child)

		elif front.is_goal:
			break

def DFS(tree):
	while not tree.is_empty():
		top = tree.pop()

		print 'node: ', top
		print 'is_goal: ', top.is_goal
		print 'node level: ', top.level
		print '\n'

		if not top.is_goal:
			if top.level == 5:
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
	root = Node(0)

	"""
		Uncomment next three lines for BFS
		Comment the three lines below
	"""
	tree = Queue()
	tree.enqueue(root)
	BFS(tree)

	"""
		Uncoment next three lines for DFS
		Comment the three lines above
	"""
	# tree = Stack()
	# tree.push(root)
	# DFS(tree)


if __name__ == '__main__':
	main()