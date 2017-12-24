class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value


class BST:
    def __init__(self):
        self.root = None

    def insert(self, item):
        y = None
        x = self.root
        while x is not None:
            y = x
            if item.value < x.value:
                x = x.left
            else:
                x = x.right
        item.parent = y
        if y is None:
            self.root = item
        elif item.value < y.value:
            y.left = item
        else:
            y.right = item

    def size(self):
        return self.size_recurr(self.root)

    def size_recurr(self, node):
        if node is None:
            return 0
        return 1 + self.size_recurr(node.left) + self.size_recurr(node.right)

    def printTree(self, item):
        if item is not None:
            self.printTree(item.left)
            print item.value
            self.printTree(item.right)

    def contains(self, node, element):
        if node is None:
            return False
        if node.value == element:
            return True
        if element < node.value:
            return self.contains(node.left, element)
        return self.contains(node.right, element)

    def smallest(self):
        x = self.root
        while x.left is not None:
            x = x.left
        return x.value

    def largest(self):
        x = self.root
        while x.right is not None:
            x = x.right
        return x.value

    def greaterSumTree(self, item):
        if item is not None:
            self.greaterSumTree(item.right)
            global sum1
            sum1 = sum1 + item.value
            item.value = sum1 - item.value
            self.greaterSumTree(item.left)


sum1 = 0
b = BST()
array = [5, 3, 9, 7, 1, 4, 0, 12, 11, 13, 15, 6, 2, 8, 10, 14]
for ele in array:
    item = Node(ele)
    b.insert(item)
b.printTree(b.root)
print "if bst contains 5"
print b.contains(b.root, 5)
print "if bst contains 21"
print b.contains(b.root, 21)
print "The smallest element in BST is"
print b.smallest()
print "The largest element in BST is"
print b.largest()
print "Size of BST is"
print b.size()
print "Before greaterSumTree"
b.printTree(b.root)
b.greaterSumTree(b.root)
print "After greaterSumTree"
b.printTree(b.root)
