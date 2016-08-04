# btree.py
"""
python implimentation of a binary tree
"""

class Node:
    """
    nodes of a binary tree
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    """
    the structure of nodes in a binart tree
    """
    def __init__(self):
        self.root = None

    def get_root(self):
        """
        return the root node of the binary tree
        """
        return self.root

    def add(self, val):
        """
        adds a value to the root or a branch
        """
        if self.root is None:
            # if the root does not exist create it
            self.root = Node(val)
        else:
            # otherwise add the node to the next left node
            self._add(val, self.root)

    def _add(self, val, node):
        """
        recurse adding of nodes to a binary tree
        """
        if val < node.value:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        """
        starts recursive finding of a value
        """
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        """
        recursivley find a value
        """
        if val is node.value:
            return node
        elif val < node.value and node.left is not None:
            self._find(val, node.left)
        elif val > node.value and node.right is not None:
            self._find(val, node.right)

    def delete_tree(self):
        """
        set the root to none and the GC will take over
        """
        self.root = None


