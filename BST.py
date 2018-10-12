# Build a Binary Search Tree from scratch using recursive
# Fill the tree with some random number

class Node:
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)


    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left is None:
                cur_node.left=Node(value)
            else:
                self._insert(value, cur_node.left)

        elif value>cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value,cur_node.right)
        else:
            print("value in the tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print (str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root,0)

    def _height(self,cur_node,cur_height):
        if cur_node is None:
            return cur_height
        left_height=self._height(cur_node.left,cur_height+1)
        right_heoght= self._height(cur_node.right, cur_height+1)
        return max(left_height,right_heoght)

    def fill_tree(self,tree,num_elems= 100,max_int=1000):
        from random import randint
        for _ in range(num_elems):
            cur_elem = randint(0,max_int)
            tree.insert(cur_elem)
        return tree

    def search(self, value):
        if self.root is not None:
            return self._search(value,self.root)
        else:return False

    def _search(self,value,cur_node):
        if value is cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value,cur_node.left)
        elif value> cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node. right)
        else:
            return False



tree = BST()
tree = tree.fill_tree(tree)

tree.print_tree()
print("tree height: "+str(tree.height()))

print(tree.search(100))