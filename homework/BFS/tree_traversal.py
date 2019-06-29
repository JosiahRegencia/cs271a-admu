from node import Node 
from queue import Queue


def BFS(tree):
	if tree.dequeue().is_goal() is False:
		print 'tree front: ', tree.front()

def main():
	root = Node(0)
	tree = Queue()
	tree.append(root)
	BFS(tree)


if __name__ == 'main':
	main()