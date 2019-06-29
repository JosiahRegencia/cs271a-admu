class Node:
    def __init__(self,key,level):
        self.level = level
        self.key = key
        self.leftChild = None
        self.middleChild = None
        self.rightChild = None
    # return the key stored in node
    def getKey(self):
        return self.key


class Tree:
    def __init__(self):
        # track number of keys
        self.keyTracker = 0
        # track depth of tree
        self.depth = 0
        # initialize fringe for BFS
        self.queue = []
        #initialize fringe for DFS
        self.stack = []
        # root of tree
        self.root = None

    def expand_bfs(self):
        # if root
        if (len(self.queue) == 0):
            # increment tracking of keys so that root node starts at 1
            self.keyTracker = self.keyTracker + 1
            # assign root node to tree object
            self.root = Node(self.keyTracker, self.depth)
            # enqueue the root node to queue
            self.queue.append(self.root)
        else:
            # get the 1st in queue, then create new node. points via leftChild
            self.queue[0].leftChild = Node(self.keyTracker+1,self.queue[0].level+1)
            # enqueue to fringe
            self.queue.append(self.queue[0].leftChild)
            # update max depth if a new level has been reached
            if (self.queue[0].level > self.depth):
                self.depth = self.queue[0].level
            # get the 1st in queue, then create new node. points via middleChild
            self.queue[0].middleChild = Node(self.keyTracker+2,self.queue[0].level+1)
            # enqueue to fringe
            self.queue.append(self.queue[0].middleChild)
            # update max depth if a new level has been reached
            if (self.queue[0].level > self.depth):
                self.depth = self.queue[0].level
            # get the 1st in queue, then create new node. points via rightChild
            self.queue[0].rightChild = Node(self.keyTracker+3,self.queue[0].level+1)
            # enqueue to fringe
            self.queue.append(self.queue[0].rightChild)
            # update max depth if a new level has been reached
            if (self.queue[0].level > self.depth):
                self.depth = self.queue[0].level
            # update the tracker (3 because 3 nodes were created)
            self.keyTracker = self.keyTracker + 3
            # dequeue the 'incorrect' node
            self.queue.pop(0)

    # DOESN'T WORK YET
    def preorder(self,root):
        if (self.root != None):
            print(self.root.key)
            self.preorder(self.root.leftChild)
            self.preorder(self.root.rightChild)

    # HAVENT TESTED PERO PARANG GOODS
    def expand_dfs(self):
        # if root
        if (len(self.stack) == 0):
            self.keyTracker = self.keyTracker + 1
            self.root = Node(self.keyTracker, self.depth)
            self.stack.append(self.root)
        else:
            temp = len(self.stack)-1
            self.stack[temp].leftChild = Node(self.keyTracker+1,self.stack[temp].level+1)
            self.stack.append(self.stack[temp].leftChild)
            if (self.stack[temp].level > self.depth):
                self.depth = self.stack[temp].level
            self.stack[temp].middleChild = Node(self.keyTracker+2,self.stack[temp].level+1)
            self.stack.append(self.stack[temp].middleChild)
            if (self.stack[temp].level > self.depth):
                self.depth = self.stack[temp].level
            self.stack[temp].rightChild = Node(self.keyTracker+3,self.stack[temp].level+1)
            self.stack.append(self.stack[temp].rightChild)
            if (self.stack[temp].level > self.depth):
                self.depth = self.stack[temp].level
            self.keyTracker = self.keyTracker + 3
            self.stack.pop(0)

    # Shows the contents of the queue to track contents and depth level
    def getQueue(self):
        for i in self.queue:
            print("key = {}, depth = {}".format(i.key, i.level))

    def getStack(self):
        for i in self.stack:
            print("key = {}, depth = {}".format(i.key, i.level))

# driver method FOR MANUAL TESTING
# test = Tree()
# test.expand_bfs()
# test.getQueue()
# test.preorder(test.root)

# driver method UPDATE THE DESIRED LEVEL INPUT
level_input = 5
test = Tree()
while (test.depth != level_input):
    test.expand_bfs()
    test.getQueue()


level_input = 2
test = Tree()

while (test.depth != level_input):
    test.expand_dfs()
    test.getStack()
