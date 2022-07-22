from dataclasses import dataclass


class TreeNode:

    data = None
    leftNode = None
    rightNode = None
    balanceFactor = 0

class AVL_Tree:
    
    def __init__(self) -> None:
        self.rootNode = TreeNode()

    def insert(self, data):
        new_node = TreeNode()
        new_node.data = data
        self.indert_at_node(self.rootNode, new_node)
        return 0

    def indert_at_node(self,currect_node: TreeNode, tree_node: TreeNode):

        if (currect_node.data == None):
            currect_node.data = tree_node.data
        
        elif(currect_node.data> tree_node.data):

            #allocate memory
            if (currect_node.leftNode == None):
                currect_node.leftNode = TreeNode()

            self.indert_at_node(currect_node.leftNode, tree_node)

        elif(currect_node.data < tree_node.data):

            #allocate memory
            if (currect_node.rightNode == None):
                currect_node.rightNode = TreeNode()

            self.indert_at_node(currect_node.rightNode, tree_node)
            
        else:
            print("Wrong data, please check the input!")
            return -1

        return 0


avt_tree = AVL_Tree()
avt_tree.insert(5)
avt_tree.insert(4)
avt_tree.insert(3)
avt_tree.insert(2)
avt_tree.insert(1)

print("end")
print("end")