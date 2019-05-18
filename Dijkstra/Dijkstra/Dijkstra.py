import math
import heapq
#from enum import Enum
#class VertexColor(Enum):
#        BLACK = 0
#        GRAY = 127
#        WHITE = 255
class Vertex:
    def __init__(self, name=None, p=None, d=None):
        self.name=name
        self.adj=[]
        self.p=p
        self.d=d
    #ove stvari moraju da budu tu da bi heapq znao kako da poredi nase objekte
    def __cmp__(self, otherVertex):
        return self.cmp(self.d, otherVertex.d)

    def __lt__(self, otherVertex):
        return self.d<otherVertex.d
    #---------------------------------------------------------------
class Edge:
    def __init__(self, v1=None, v2=None, weight=None):
        self.weight=weight
        self.v1=v1
        self.v2=v2
def init(G, s):
    for v in G:
        v.d=math.inf
        v.p=None
    s.d=0

def Dijkstra(G, s):
    init(G, s)
    Q=[]
    heapq.heappush(Q, s)
    while(len(Q)>0):
        u=heapq.heappop(Q)
        for edge in u.adj:
            #relax fja samo sto nije fja :p
            u=edge.v1
            v=edge.v2
            newDist=u.d+edge.weight
            if newDist<v.d:
                v.p=u
                v.d=newDist
                heapq.heappush(Q, v)
            #------------------------------
def get_shortest_path(target):
    a=target
    l=[]
    while a is not None:
        l.append(a.name)
        a=a.p
    l.reverse()
    print("Shortest path to target is", target.d, ", it goes through nodes", l)
v1=Vertex(name=1)
v2=Vertex(name=2)
v3=Vertex(name=3)
v4=Vertex(name=4)
v5=Vertex(name=5)
v1.adj=[Edge(v1, v2, 2), Edge(v1, v3, 1), Edge(v1, v4, 6)]
v2.adj=[Edge(v2, v5, 5), Edge(v2, v4, 3)]
v3.adj=[Edge(v3, v4, 2)]
v4.adj=[Edge(v4, v5, 2)]
G=[v1, v2, v3, v4, v5]
Dijkstra(G, v1)
get_shortest_path(v5)