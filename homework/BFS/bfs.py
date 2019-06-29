from node import Node 
from queue import Queue


def BFS(tree):
	while not tree.is_empty():
		front = tree.dequeue()
		
		if front.level > 5:
			break

		print 'node: ', front
		print 'node level: ', front.level
		print '\n'

		if not front.is_goal():
			children = front.create_children(3)
			for child in children:
				tree.enqueue(child)

		elif front.is_goal():
			break

def main():
	root = Node(0)
	tree = Queue()
	tree.enqueue(root)
	BFS(tree)


if __name__ == '__main__':
	main()