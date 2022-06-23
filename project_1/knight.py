# dimensions of the board
import random

n = 3
m = 3

class Knight:
    def __init__(self):
        self.location = self.set_location()

    def set_location(self):
        loc = random.randint(0,2),random.randint(0,2)

        while loc[0] == 1 and loc[1] == 1:
            loc = random.randint(0,2),random.randint(0,2)
        return loc

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
            if ((x >= 0 and y >= 0) and (x < n and y < m)):
                count += 1
                output.append([X[i],Y[i]])
        return output
