# dimensions of the board
# https://www.geeksforgeeks.org/possible-moves-knight/?fbclid=IwAR3LIu01zCrrWsV1BQryIvS3sd2clQ41tRc3GOhFNTxEfAf4Q6qcKExcpr0
n = 4
m = 4

class Knight:
    def __init__(self, start_x, start_y):
        self.location = [start_x,start_y]

    # successor function
    def update_state(self,level,current):
        self.location = [level,current]

    def possible_moves(self,p,q):
        X = [2,1,-1,-2,-2,-1,1,2]
        Y = [1,2,2,1,-1,-2,-2,-1]
        count = 0
        output = []
        for i in range(8):
            x = p + X[i]
            y = q + Y[i]
            if (x >= 0 and y >= 0 and x < n and y < m):
                count += 1
                output.append([X[i],Y[i]])
        return output
