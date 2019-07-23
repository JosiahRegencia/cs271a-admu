class cell:
	def __init__(self, x = 0, y = 0, distance = 0):
		self.x = x
		self.y = y
		self.distance = distance

def heuristic(origin, target, N):
	move_x = [2,1,-1,-2,-2,-1,1,2]
	move_y = [1,2,2,1,-1,-2,-2,-1]

	queue = []
	queue.append(cell(origin[0], origin[1], 0))

	visited = [[False for i in range(N + 1)] for j in range(N + 1)]
	visited[origin[0]][origin[1]] = True

	while(len(queue) > 0):
		item = queue[0]
		queue.pop(0)
		if(item.x == target[0] and
		item.y == target[1]):
			return item.distance
		# iterate for all reachable states
		for i in range(8):
			x = item.x + move_x[i]
			y = item.y + move_y[i]
			if((x >= 0 and x < N and y >= 0 and y < N) and not visited[x][y]):
				visited[x][y] = True
				queue.append(cell(x, y, item.distance + 1))
