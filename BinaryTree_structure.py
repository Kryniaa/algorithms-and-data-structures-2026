class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:  
    def __init__(self):
        self.root = None
    
    def search(self, key):
        node_ptr = self.root
        while node_ptr is not None:
            if node_ptr.key == key:
                return node_ptr.value
            elif key < node_ptr.key:
                node_ptr = node_ptr.left
            else:
                node_ptr = node_ptr.right
        return None
    
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
            return
        
        current = self.root
        while current:
            if current.key == key:
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = TreeNode(key, value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(key, value)
                    return
                current = current.right

    def delete(self, key):
        parent = None
        current = self.root

        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None: 
            raise Exception("Not found")

        if current.left and current.right:
            succ_parent = current
            successor = current.right
            while successor.left:
                succ_parent = successor
                successor = successor.left
            
            current.key = successor.key
            current.value = successor.value
            
            current = successor
            parent = succ_parent

        child = current.left if current.left else current.right
        
        if parent is None:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self.__print_tree(node.left, lvl + 5)

    def print_as_list(self):
        self._in_order_walk(self.root)
        print()

    def _in_order_walk(self, node):
        if node is not None:
            self._in_order_walk(node.left)
            print(f"{node.key} {node.value}, ", end="")
            self._in_order_walk(node.right)
    
    def height(self):
        return self._calculate_height(self.root)

    def _calculate_height(self, node):
        if node is None:
            return -1
        l_h = self._calculate_height(node.left)
        r_h = self._calculate_height(node.right)
        return 1 + max(l_h, r_h)

def main():
    tree = BST()
    tree.insert(50,'A')
    tree.insert(15,'B')
    tree.insert(62,'C')
    tree.insert(5,'D')
    tree.insert(20,'E')
    tree.insert(58,'F')
    tree.insert(91,'G')
    tree.insert(3,'H')
    tree.insert(8,'I')
    tree.insert(37,'J')
    tree.insert(60,'K')
    tree.insert(24,'L')
    tree.print_tree()
    print(tree.search(24))
    tree.insert(20,"AA")
    tree.insert(6,"M")
    tree.delete(62)
    tree.insert(59,"N")
    tree.insert(100,"P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55,"R")
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print_as_list()
    tree.print_tree()
    
if __name__ == "__main__":
    main()