#python avl tree by Guangbei

class TreeNode:

    data = None
    leftNode = None
    rightNode = None
    height = -1

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

            #update tree height
            self.check_tree_height(self.rootNode)

            #self.rootNode = self.balance(self.rootNode)

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

        if (currect_node.data == self.rootNode.data):
            currect_node = self.balance(currect_node)
            self.rootNode = currect_node
        else:
            currect_node = self.balance(currect_node)
            print(currect_node.data)

        return 0

    def check_heigh(self, current_node: TreeNode):

        if (current_node != None):

            if(current_node.leftNode != None and current_node.rightNode != None):

                return max(self.check_heigh(current_node.leftNode), self.check_heigh(current_node.rightNode)) + 1

            elif(current_node.leftNode != None and current_node.rightNode == None):

                return self.check_heigh(current_node.leftNode) + 1

            elif(current_node.rightNode != None and current_node.leftNode == None):

                return self.check_heigh(current_node.rightNode) + 1

            else:
                return 0

        return 0

    def check_tree_height(self, current_node: TreeNode):

        current_node.height = self.check_heigh(current_node)

        if (current_node.leftNode != None):

            self.check_tree_height(current_node.leftNode)

        if (current_node.rightNode != None):

            self.check_tree_height(current_node.rightNode)

        return 0

    def get_node_height(self, current_node: TreeNode):
        return -1 if current_node == None else current_node.height

    def rotate_with_left_child(self, current_node: TreeNode):

        temp_node = current_node
        current_node = current_node.leftNode
        
        temp_node.leftNode = current_node.rightNode
        current_node.rightNode = temp_node

        self.check_tree_height(current_node)

        return current_node

    def rotate_with_right_child(self, current_node: TreeNode):

        temp_node = current_node
        current_node = current_node.rightNode

        temp_node.rightNode = current_node.leftNode
        current_node.leftNode = temp_node

        self.check_tree_height(current_node)

        return current_node

    def double_with_left_chlid(self, current_node: TreeNode):

        current_node.leftNode = self.rotate_with_right_child(current_node.leftNode)
        current_node = self.rotate_with_left_child(current_node)

        return current_node
    
    def double_with_right_chlid(self, current_node: TreeNode):

        current_node.rightNode = self.rotate_with_left_child(current_node.rightNode)
        current_node = self.rotate_with_right_child(current_node)

        return current_node

    def balance(self, current_node: TreeNode):

        ALLOWED_IMBALANCE = 1

        if (current_node == None):
            return 0

        if (self.get_node_height(current_node.leftNode)  - self.get_node_height(current_node.rightNode) > ALLOWED_IMBALANCE):
            if (self.get_node_height(current_node.leftNode.leftNode) >= self.get_node_height(current_node.leftNode.rightNode)):
                current_node = self.rotate_with_left_child(current_node)
            else:
                current_node = self.double_with_left_chlid(current_node)

        if (self.get_node_height(current_node.rightNode)  - self.get_node_height(current_node.leftNode) > ALLOWED_IMBALANCE):
            if (self.get_node_height(current_node.rightNode.rightNode) >= self.get_node_height(current_node.rightNode.leftNode)):
                current_node = self.rotate_with_right_child(current_node)
            else:
                current_node = self.double_with_right_chlid(current_node)

        self.check_tree_height(current_node)
        return current_node




avt_tree = AVL_Tree()
avt_tree.insert(5)
avt_tree.insert(4)
avt_tree.insert(3)
avt_tree.insert(2)
avt_tree.insert(1)

print("end")