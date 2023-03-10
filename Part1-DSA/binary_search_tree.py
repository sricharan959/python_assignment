class BSTree():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
    
def insert(node,key,value):
    if node is None:
        node=BSTree(key,value)
    elif key<node.key:
        node.left=insert(node.left,key,value)
        node.left.parent=node
    elif key>node.key:
        node.right=insert(node.right,key,value)
        node.right.parent=node
    return node

def delete(node,key):
    if node is None:
        return node
    if key<node.key:
        node.left=delete(node.left,key)
    elif key>node.key:
        node.right=delete(node.right,key)
    else:
        if node.left is None:
            temp=node.right
            node=None
            return temp
        if node.right is None:
            temp=node.left
            node=None
            return temp
        
        current = node
        while(current.left is not None):
            current = current.left
        temp=current
        node.key=temp.key
        node.right=delete(node.right,temp.key)
    return node

def search(node,key):
    if node is None:
        return None
    elif node.key==key:
        return node.key==key
    elif key<node.key:
        return search(node.left,key)
    elif key>node.key:
        return search(node.right,key)
    
def size(node):
    if node is None:
        return 0
    return 1+size(node.left)+size(node.right)