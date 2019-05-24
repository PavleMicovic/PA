from enum import Enum
import math	
import heapq
import random
class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, name = None, p = None, d=None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.name = name
        self.p = p
        self.d=d
        self.adj=[]
    def __cmp__(self, other):
        return self.cmp(self.d, other.d)
    def __lt__(self, other):
        return self.d<other.d
class Edge:
    def __init__(self, startv=None, endv=None, w=None):
        self.s=startv
        self.e=endv
        self.w=w    #weight
def add_edge(startv, endv, weight):
    startv.adj.append(Edge(startv, endv, weight))
def init(G, s):
    for v in G:
        v.d=math.inf
        v.p=None
    s.d=0
def dijkstra(G, s):
    init(G, s)
    Q=[]
    heapq.heapify(Q)
    heapq.heappush(Q, s)
    while(len(Q)!=0):
        u=heapq.heappop(Q)
        for edge in u.adj:
            relax(edge, Q)
def relax(edge, Q):
    u=edge.s
    v=edge.e
    newDist=u.d+edge.w
    if v.d>newDist:
        v.d=newDist
        v.p=u
        heapq.heappush(Q, v)
def print_shortest_path(target):
    a=target
    l=[]
    if(target.d==math.inf):
        print("Its impossible to reach node", target.name,"from your starting point")
        return
    while a is not None:
        l.append(a.name)
        a=a.p
    l.reverse()
    print("Shortest distance to ", target.name, "is", target.d, "and it goes through nodes", l)
def random_graph(G):
    for i in G:
        b=random.randint(1, 5)#nasumican broj veza koji poticu iz ovog cvora
        j=0
        ind=0
        while j<b:
            a=random.choice(G)#veza sa nasumicnim cvorom iz grafa
            c=random.randint(1, 15)#nasumicna tezina veze
            for it in i.adj:
                if (it.e.name==a.name):
                    ind=1
                    break
                else:
                    ind=0
            if(ind==0):
                add_edge(i, a, c)
            j+=1
def draw_graph(G):
    for i in G:
        for j in i.adj:
            print(i.name, "->", j.e.name, "weight: ", j.w)
        print("--------------------------------\n")
s=Vertex(name="s")
t=Vertex(name="t")
y=Vertex(name="y")
x=Vertex(name="x")
z=Vertex(name="z")
beskonacno=Vertex(name="n")
G=[s, t, y, x, z, beskonacno]
random_graph(G)
# ivice iz s
#add_edge(s, t, 10)
#add_edge(s, y, 5)
#----------------------

#ivice iz y
#add_edge(y, t, 3)
#add_edge(y, z, 2)
#add_edge(y, x, 9)
#----------------------

#ivice iz t
#add_edge(t, y, 2)
#add_edge(t, x, 1)
#----------------------

#ivice iz x
#add_edge(x, z, 4)
#----------------------

#ivice iz z
#add_edge(z, s, 7)
#add_edge(z, x, 6)
#----------------------

#G=[s, t, x, y, z, beskonacno]
startv=random.choice(G)
dijkstra(G, startv)
draw_graph(G)
print("-------------------------\nStarting point is", startv.name, "\n--------------------")
print_shortest_path(t)
print_shortest_path(y)
print_shortest_path(x)
print_shortest_path(z)
print_shortest_path(beskonacno)
print_shortest_path(s)
