Group members:
	Qui, Christian
	Regencia, Josiah Eleazar


Requirements:
1. Python2.7.* or Python3

Notes on how to run the homework:

1. Main file is tree_traversal.py
2. Running tree_traversal.py accepts an argument to select whether the program will run a dfs or a bfs.
 	2.1 To run bfs: python tree_traversal.py bfs
 	2.2 To run dfs: python tree_traversal.py dfs
3. The arguments 'dfs' or 'bfs' are not case-sensitive. So it can be DFS or Dfs.


Notes on implementation:
1. For this homework, we initially decided that the basis whether a node was a goal state is a random boolean.
	1.1 Node is a goal state if goal instant variable is True. False if otherwise
2. In this implementation, each node has a 5% chance to be a goal state (1/20)
3. The children of a node is implemented as a list. This helps in making the branching factor dynamicc
	3.1 children[0] is implemented as the leftmost side of the list
	3.2 children[length-1] is implemented as the rightmost side of the list
4. DFS and BFS functions have the same implementation. The only differences:
	4.1 Data struture that was used for each traversal
	4.2 The placement of the level tracker
