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
	depth = 0
	while not tree.is_empty():
		depth += 1
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
	return depth



def BFS(tree, depth_level, Knight, Enemy):
	depth = 0
	while not tree.is_empty():
		depth += 1
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
	return depth

def DFS(tree, depth_level, Knight, Enemy):
	depth = 0
	while not tree.is_empty():
		depth += 1
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
	return depth

def main():
	commands = ['bfs', 'dfs', 'greedy', 'all']
	knight = Knight()
	print('Knight Location: {}'.format(knight.location))

	black_knight = Knight()
	print('Enemy Location: {}'.format(black_knight.location))
	print('\n\n')

	# root = Node(None, knight.location[0],knight.location[1])

	
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
	bfs_depth = BFS(tree, 3, knight, black_knight)
	end_bfs = time.time()

	# dfs
	print('\n----DFS Traversal----')
	start_dfs = time.time()
	tree = Stack()
	tree.push(root_dfs)
	dfs_depth = DFS(tree, 3, knight, black_knight)
	end_dfs = time.time()

	# greedy
	print('\n----Greedy Best First Search Traversal----')
	start_greedy = time.time()
	tree = PriorityQueue()
	tree.enqueue(root_informed)
	greedy_depth = GreedyBFS(tree, 3, knight, black_knight)
	end_greedy = time.time()

	# output
	print("\n\n")
	print("BFS:\t{0:.10f}\tDepth: {1}".format(end_bfs-start_bfs, bfs_depth))
	print("DFS:\t{0:.10f}\tDepth: {1}".format(end_dfs-start_dfs, dfs_depth))
	print("Greedy:\t{0:.10f}\tDepth: {1}".format(end_greedy-start_greedy, greedy_depth))


if __name__ == '__main__':
	main()
