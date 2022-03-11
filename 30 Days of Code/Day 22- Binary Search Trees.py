class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root == None or root.left == root.right == None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    # def getHeight(self, root):
    #     # Write your code here
    #     # If we have reached a leaf node return 0 because we cannot traverse any more
    #     # edges
    #     if root.left == None and root.right == None:
    #         return 0
    #
    #     # Initialize both depths of left-subtree and right-subtree to 0
    #     # So it becomes easy for max() function line written below
    #     leftDepth = rightDepth = 0
    #
    #     # If node has a left child, get its left-subtree depth
    #     if root.left != None:
    #         # Every time you are able to go one node to the left
    #         # you are traversing an edge, so you are adding 1 to its leftDepth
    #         leftDepth = 1 + self.getHeight(root.left)
    #         # Whatever I wrote above but change left to right
    #     if root.right != None:
    #         rightDepth = 1 + self.getHeight(root.right)
    #
    #     # Once you reach this stage, it means it wasn't a leaf node and depths of
    #     # left and right subtrees have been found so just return the max of the two
    #     # and that will be the maxHeight for the node root
    #     return max(leftDepth, rightDepth)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
