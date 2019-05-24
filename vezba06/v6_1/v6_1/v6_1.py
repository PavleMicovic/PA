class Podatak:
    def __init__(self, v=None, f=None, l=None, r=None, p=None):
        self.value=v
        self.freq=f
        self.left=l
        self.right=r
        self.parent=p

def get_histogram(niz):
    a=[]
    b=[]
    for i in niz:
        if i not in a:
            a.append(i)
    for i in a:
        b.append(Podatak(v=i, f=1))
    for i in b:
        i.freq=niz.count(i.value)
    return b
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i>=0 and A[i].freq>key.freq):
            A[i+1]= A[i]
            i = i - 1
        A[i+1] = key

def get_min_freq_el(l):
    return l[0]
def remove_elem(l):
    l.remove(l[0])
def make_new_el(e1, e2):
    if e1.freq>e2.freq:
        e=Podatak(v=e1.value+e2.value,f=e1.freq+e2.freq,l=e2,r=e1)
        e1.parent=e
        e2.parent=e
    else:
        e=Podatak(v=e1.value+e2.value,f=e1.freq+e2.freq,l=e1,r=e2)
        e1.parent=e
        e2.parent=e
    return e
def put_elem(l,e):
    l.append(e)
    insertion_sort(l)
def in_order_tree_walk(root):
    if root!=None:
        in_order_tree_walk(root.left)
        print(root.freq)
        in_order_tree_walk(root.right)
def generisanje_koda(root, elem):
    s="0"
    while(root!=None and elem!=root.freq):
        if(elem<root.freq):
            s+='0'
            root=root.left
        else:
            s+='1'
            root=root.right
    return s
input1 = ['a', 'b']
#print(input1)

input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
#print(input2)

input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
#print(input3)

input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
#print(input4)

input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
#print(input5)

l=get_histogram(input5)
insertion_sort(l)
for i in range(len(l)):
        print(l[i].value, l[i].freq)
while len(l)>1:
    print("\nNOVI KORAK\n")
    e1=get_min_freq_el(l)
    print("Min element 1:",e1.freq)
    remove_elem(l)
    e2=get_min_freq_el(l)
    print("Min element 2:",e2.freq)
    remove_elem(l)
    e=make_new_el(e1,e2)
    print("Novi element:",e.freq, "\nLevi element tj min1:",e.left.freq, "\nDesni element tj min2:",e.right.freq,"\n")
    put_elem(l,e)
    for i in range(len(l)):
        print(l[i].value, l[i].freq)
print("\n")
in_order_tree_walk(l[0])
print("\n------------------------------------------------------------\n")
n=6
s=generisanje_koda(l[0], n)
print("Generisan kod:", s, "\nVrednost:", n)
