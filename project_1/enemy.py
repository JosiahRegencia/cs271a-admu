import random


class Enemy:
    def __init__(self):
        self.location = [self.set_location()[0], self.set_location()[1]]
        # self.isDead = False

    def set_location(self):
    	loc = random.randint(0,2),random.randint(0,2)
    	print 'loc: ', loc
    	print 'is_equal: ', loc==(1,1)

    	while loc[0] == 1 and loc[1] == 1:
    		loc = random.randint(0,2),random.randint(0,2)
    	return loc
