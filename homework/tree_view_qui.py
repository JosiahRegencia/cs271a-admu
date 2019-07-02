class TreeView:
    def __init__(self):
        self.levels = []

    def add_node(self, level):
        self.levels[level] = self.levels[level] + level

    def print_tree(self):
        print(self.levels)
