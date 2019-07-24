from node_uninformed import Node
from node_informed import Node_informed
from stack import Stack
from queue import Queue
from tree_view import TreeView
from knight import Knight
from heuristic import heuristic
from heuristic import cell
import random
from priority_queue import PriorityQueue

import sys
import time


def GreedyBFS(tree, depth_level, Knight, Enemy):
	while not tree.is_empty():
		front = tree.dequeue()
		Knight.update_state(front.level,front.current)
		if Knight.location[0] > depth_level:
			break
		print('current state: {} {}\tgoal state: {} {}'.format(Knight.location[0],Knight.location[1],
														 Enemy.location[0],Enemy.location[1]))

		if not front.is_goal(Knight,Enemy):
			children = front.create_children(Knight, Enemy)
			for child in children:
				tree.enqueue(child)

		elif front.is_goal(Knight,Enemy):
			break



def BFS(tree, depth_level, Knight, Enemy):
	while not tree.is_empty():
		front = tree.dequeue()
		Knight.update_state(front.level,front.current)
		if Knight.location[0] > depth_level:
			break
		print('current state: {} {}\tgoal state: {} {}'.format(Knight.location[0],Knight.location[1],
														 Enemy.location[0],Enemy.location[1]))

		if not front.is_goal(Knight,Enemy):
			children = front.create_children(Knight)
			for child in children:
				tree.enqueue(child)

		elif front.is_goal(Knight,Enemy):
			break

def DFS(tree, depth_level, Knight, Enemy):
	while not tree.is_empty():
		top = tree.pop()
		Knight.update_state(top.level,top.current)
		print('current state: {} {}\tgoal state: {} {}'.format(Knight.location[0],Knight.location[1],
														 Enemy.location[0],Enemy.location[1]))

		if not top.is_goal(Knight,Enemy):
			if top.level == depth_level:
				continue
			else:
				children = top.create_children(Knight)
				for child in children[::-1]:
					tree.push(child)

		elif top.is_goal(Knight,Enemy):
			break

def main():
	commands = ['bfs', 'dfs', 'greedy', 'all']
	knight = Knight()
	print('Knight Location: {}'.format(knight.location))

	black_knight = Knight()
	print('Enemy Location: {}'.format(black_knight.location))
	print('\n\n')

	# root = Node(None, knight.location[0],knight.location[1])

	try:
		traversal = sys.argv[1].lower()
		if traversal == commands[0]:
			root = Node(None, knight.location[0],knight.location[1])
			start = time.time()
			tree = Queue()
			tree.enqueue(root)
			BFS(tree, 3, knight, black_knight)
			end = time.time()
			print('\nTotal Traverse Time:\t{}'.format(end-start))
		elif traversal == commands[1]:
			root = Node(None, knight.location[0],knight.location[1])
			start = time.time()
			tree = Stack()
			tree.push(root)
			DFS(tree, 3, knight, black_knight)
			end = time.time()
			print('\nTotal Traverse Time:\t{}'.format(end-start))
		elif traversal == commands[2]:
			root = Node_informed(None, knight.location[0],knight.location[1],heuristic(knight.location,black_knight.location,3))
			start = time.time()
			tree = PriorityQueue()
			tree.enqueue(root)
			GreedyBFS(tree, 3, knight, black_knight)
			end = time.time()
			print('\nTotal Traverse Time:\t{}'.format(end-start))
		# output all
		elif traversal == commands[3]:
			# several roots were made to ensure initialization of Knight
			# bfs might end up updating the knight, leaving the knight in goal state for the succeeding trials
			root_bfs = Node(None, knight.location[0],knight.location[1])
			root_dfs = Node(None, knight.location[0],knight.location[1])
			root_informed = Node_informed(None, knight.location[0],knight.location[1],heuristic(knight.location,black_knight.location,3))

			# bfs
			print('----BFS Traversal----')
			start_bfs = time.time()
			tree = Queue()
			tree.enqueue(root_bfs)
			BFS(tree, 3, knight, black_knight)
			end_bfs = time.time()

			# dfs
			print('----DFS Traversal----')
			start_dfs = time.time()
			tree = Stack()
			tree.push(root_dfs)
			DFS(tree, 3, knight, black_knight)
			end_dfs = time.time()

			# greedy
			print('----Greedy Best First Search Traversal----')
			start_greedy = time.time()
			tree = PriorityQueue()
			tree.enqueue(root_informed)
			GreedyBFS(tree, 3, knight, black_knight)
			end_greedy = time.time()

			# output
			print("BFS: {0:.4f}".format(end_bfs-start_bfs))
			print("DFS: {0:.4f}".format(end_dfs-start_dfs))
			print("Greedy: {0:.4f}".format(end_greedy-start_greedy))
		else:
			print('Only \'BFS\' or \'DFS\' allowed arguments')
	except IndexError as error:
		print(' Error: ', error)
		print('Must pass \'BFS\' or \'DFS\' as argument')


if __name__ == '__main__':
	main()
