from node import Node
from stack import Stack
from queue import Queue
from tree_view_qui import TreeView

import sys



def BFS(tree, depth_level):
	treeview = TreeView()
	while not tree.is_empty():
		front = tree.dequeue()
		treeview.add_node(front.level)
		if front.level > depth_level:
			break

		print('node: {}\tis_goal: {}\tnode level: {}'.format(front, front.is_goal, front.level))

		if not front.is_goal:
			children = front.create_children(3)
			for child in children:
				tree.enqueue(child)

		elif front.is_goal:
			break
	return treeview

def DFS(tree, depth_level):
	treeview = TreeView()
	while not tree.is_empty():
		top = tree.pop()
		treeview.add_node(top.level)

		print('node: {}\tis_goal: {}\tnode level: {}'.format(top, top.is_goal, top.level))

		if not top.is_goal:
			if top.level == depth_level:
				continue
			else:
				children = top.create_children(3)
				for child in children[::-1]:
					tree.push(child)

		elif top.is_goal:
			break
	return treeview

def main():
	commands = ['bfs', 'dfs']
	root = Node(0)

	try:
		traversal = sys.argv[1].lower()
		if traversal == commands[0]:
			tree = Queue()
			tree.enqueue(root)
			BFS(tree, 5).print_tree
		elif traversal == commands[1]:
			tree = Stack()
			tree.push(root)
			DFS(tree, 5).print_tree
		else:
			print('Only \'BFS\' or \'DFS\' allowed arguments')
	except IndexError as error:
		print(' Error: ', error)
		print('Must pass \'BFS\' or \'DFS\' as argument')

if __name__ == '__main__':
	main()
