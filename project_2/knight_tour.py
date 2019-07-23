from node import Node
from stack import Stack
from queue import Queue
from tree_view import TreeView
from knight import Knight
from heuristic import heuristic
from heuristic import cell
import heapq
import random

import sys
import time


def priority_queue(tree, depth_level, Knight, Enemy):
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
	commands = ['bfs', 'dfs']
	knight = Knight()
	print('Knight Location: {}'.format(knight.location))

	black_knight = Knight()
	print('Enemy Location: {}'.format(black_knight.location))
	print('\n\n')

	root = Node(None, knight.location[0],knight.location[1])

	try:
		traversal = sys.argv[1].lower()
		if traversal == commands[0]:
			start = time.time()
			tree = Queue()
			tree.enqueue(root)
			BFS(tree, 3, knight, black_knight)
			end = time.time()
			print('\nTotal Traverse Time:\t{}'.format(end-start))
		elif traversal == commands[1]:
			start = time.time()
			tree = Stack()
			tree.push(root)
			DFS(tree, 3, knight, black_knight)
			end = time.time()
			print('\nTotal Traverse Time:\t{}'.format(end-start))
		else:
			print('Only \'BFS\' or \'DFS\' allowed arguments')
	except IndexError as error:
		print(' Error: ', error)
		print('Must pass \'BFS\' or \'DFS\' as argument')


if __name__ == '__main__':
	main()
