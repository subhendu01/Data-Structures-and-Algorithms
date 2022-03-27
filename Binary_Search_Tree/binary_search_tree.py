class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # search
    def search(self, target):
        if self.data == target:
            print('Found it')
            return self
        if self.left and self.data > target:
            return self.left.search(target)
        if self.right and self.data < target:
            return self.right.search(target)
        print("Didn't find the value in the tree")

    # traverse
    def traversePreorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.data)

    def getNodeAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodeAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.getNodeAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        return nodes

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

# meta data or helper function
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1) + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodeAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

    def search(self, target):
        return self.root.search(target)

    def traversePreorder(self):
        return self.root.traversePreorder()

    def traverseInorder(self):
        return self.root.traverseInorder()

    def traversePostorder(self):
        return self.root.traversePostorder()

    def getNodeAtDepth(self, depth):
        return self.root.getNodeAtDepth(depth)

    def height(self):
        return self.root.height()


# node = Node(10)
# node.left = Node(5)
# node.right = Node(15)
# node.left.left = Node(2)
# node.left.right = Node(6)
# node.right.left = Node(12)
# node.right.right = Node(20)
# print(node.right.data)
# print(node.right.right.data)

# myTree = Tree(node, 'Binary Tree')
# print(myTree.name)
# print(myTree.root.left.data)
# print(myTree.root.right.right.data)

# search
# find = myTree.root.search(20)
# find = myTree.search(20)
# print(find.data)

# Traverse
# print("Traverse Pre-Order")
# myTree.traversePreorder()
# print("Traverse In-Order")
# myTree.traverseInorder()
# print("Traverse Post-Order")
# myTree.traversePostorder()

# height
# print(myTree.root.height())
# tree = Tree(Node(400), 'Very short Tree')
# print(tree.height())

# getting all nodes at a particular depth
tree = Tree(Node(50), 'Get all node at depth')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(13)
tree.root.left.right = Node(35)
tree.root.left.right.right = Node(37)
tree.root.right.left = Node(55)
tree.root.right.right = Node(103)
tree.root.left.left.left = Node(2)
tree.root.left.left.right = Node(20)
tree.root.right.left = Node(55)
tree.root.right.right.right = Node(256)

# print(tree.getNodeAtDepth(3))

tree.print()