import random
class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
class T:
    def __init__(self, r=None):
        self.root=r
        if(self.root==None):
            self.num=0
        else:
            self.num=1
def tree_insert(T, z):
    y=None
    x=T.root
    while(x!=None):
        y=x
        if z.data.a2<x.data.a2:
            x=x.left
        else:
            x=x.right
    z.parent=y
    if y==None:
        T.root=z
    elif z.data.a2<y.data.a2:
        y.left=z
    else:
        y.right=z
    T.num+=1
def inorder_tree_walk(x, niz):
    if x!=None:
        inorder_tree_walk(x.left)
        niz.append(x)
        inorder_tree_walk(x.right)
def tree_search(x, k):
    while x!=None and k!=x.data.a2:
        if k<x.data.a2:
            x=x.left
        else:
            x=x.right
    return x
def tree_minimum(x):
    while x.left!=None:
        x=x.left
    return x
def tree_maximum(x):
    while x.right!=None:
        x=x.right
    return x
def tree_successor(x):
    if x.right!=None:
        return tree_minimum(x.right)
    y=x.parent
    while y!=None and x==y.right:
        x=y
        y=y.parent
    return y
def tree_transplant(T,u,v):
    if u.parent==None:
        T.root=v
    elif u==u.parent.left:
        u.parent.left=v
    else:
        u.parent.right=v
    if v!=None:
        v.parent=u.parent
def tree_delete(T,z):
    if z.left==None:
        tree_transplant(T,z,z.right)
    elif z.right==None:
        tree_transplant(T,z,z.left)
    else:
        y=tree_minimum(z.right)
    if y.parent!=z:
        tree_transplant(T,y,y.right)
        y.right=z.right
        y.right.parent=y
    tree_transplant(T,z,y)
    y.left=z.left
    y.left.parent=y

d = Data(1, 2)
n1=Node(d=d)
n2=Node(d=Data(3,5))
n3=Node(d=Data(68, 255))
n4=Node(d=Data(2, 33))
n5=Node(d=Data(1, 2))
n6=Node(d=Data(6, 68))
n7=Node(d=Data(5, 7))
t=T()
#tree_insert(t, n2)
#tree_insert(t, n1)
#tree_insert(t, n3)
#tree_insert(t, n4)
#tree_insert(t, n5)
#tree_insert(t, n6)
#tree_insert(t, n7)
#inorder_tree_walk(n2)
#print("Stablo ima", t.num, "elemenata")
#k=input("Koji element zelite da pronadjete?\n")
#search=tree_search(n2,int(k))
#print(search.data.a1,search.data.a2)
#a=tree_successor(n2)
#print(a.data.a1, a.data.a2)\
niz=[]
niz1=random.sample(range(300), 15)
print(niz1)
for i in range(len(niz)):
    niz[i].append(Node(d=niz1[i]))
    print(niz[i].data.a2)