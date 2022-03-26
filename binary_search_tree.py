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


    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

# meta data or helper function
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traversePreorder(self):
        return self.root.traversePreorder()

    def traverseInorder(self):
        return self.root.traverseInorder()

    def traversePostorder(self):
        return self.root.traversePostorder()

    def height(self):
        return self.root.height()


node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(2)
node.left.right = Node(6)
node.right.left = Node(12)
node.right.right = Node(20)
# print(node.right.data)
# print(node.right.right.data)
myTree = Tree(node, 'Binary Tree')
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
print(myTree.root.height())
tree = Tree(Node(400), 'Very short Tree')
print(tree.height())

