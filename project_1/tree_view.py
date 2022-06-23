class TreeView:
    def __init__(self):
        self.levels = {}

    def add_node(self, level):
        if (self.levels.get(level) == None):
            self.levels[level] = str(level)
        else:
            self.levels[level] = self.levels[level] + str(level)

    def print_tree(self):
        size = len(self.levels)
        for i in range(0,size):
            print((" ")*int((243-(3**i))/2),self.levels.get(i))
