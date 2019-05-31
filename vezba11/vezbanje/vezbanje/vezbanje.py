import math
class Vertex:
    def __init__(self, name=None):
        self.name=name
        self.p=None
        self.adj=[]
        self.d=math.inf
        self.indeg=[]
class Edge:
    def __init__(self, startv=None, endv=None, weight=None):
        self.startv=startv
        self.endv=endv
        self.w=weight
class Graph:
    def __init__(self, V=[], E=[]):
        self.V=V
        self.E=E
def add_edge(startv, endv, weight):
    startv.adj.append(Edge(startv, endv, weight))
def add_indeg(ovde, odakle):
    ovde.indeg.append(odakle)
def MakeGraph():
    a=Vertex("a")
    b=Vertex("b")
    c=Vertex("c")
    d=Vertex("d")
    e=Vertex("e")
    f=Vertex("f")
    g=Vertex("g")
    add_edge(a, b, 8)
    add_indeg(b, a)
    add_edge(a, c, 6)
    add_indeg(c, a)
    add_edge(b, d, 10)
    add_indeg(d, b)
    add_edge(c, d, 15)
    add_indeg(d, c)
    add_edge(c, e, 9)
    add_indeg(e, c)
    add_edge(d, f, 4)
    add_indeg(f, d)
    add_edge(d, e, 14)
    add_indeg(e, d)
    add_edge(e, f, 13)
    add_indeg(f, e)
    add_edge(e, g, 17)
    add_indeg(g, e)
    add_edge(f, g, 7)
    add_indeg(g, f)
    return Graph(V=[a, b, c, d, e, f, g], E=[Edge(a, b, 8), Edge(a, c, 6), Edge(b, d, 10), Edge(c, d, 15), Edge(c, e, 9), Edge(d, f, 4), Edge(d, e, 14), Edge(e, f, 13), Edge(e, g, 17), Edge(f, g, 7)])
def GetInDeg(G):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    for i in G.V:
        for j in range(len(i.indeg)):
            if i.name=="a":
                a+=1
            elif i.name=="b":
                b+=1
            elif i.name=="c":
                c+=1
            elif i.name=="d":
                d+=1
            elif i.name=="e":
                e+=1
            elif i.name=="f":
                f+=1
            elif i.name=="g":
                g+=1
    return [a, b, c, d, e, f, g]
def GetOutDeg(G):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    for i in G.V:
        for j in range(len(i.adj)):
            if i.name=="a":
                a+=1
            elif i.name=="b":
                b+=1
            elif i.name=="c":
                c+=1
            elif i.name=="d":
                d+=1
            elif i.name=="e":
                e+=1
            elif i.name=="f":
                f+=1
            elif i.name=="g":
                g+=1
    return [a, b, c, d, e, f, g]
#----------------------------------------------
def init(G, s):
    for v in G.V:
        v.d=math.inf
        v.p=None
    s.d=0
#---------------------------------------------
def relax(edge):
    u=edge.startv
    v=edge.endv
    w=edge.w
    newDist=u.d+w
    if v.d>newDist:
        v.d=newDist
        v.p=u
#----------------------------------------------
def Bellman(G, s):
    init(G, s)
    for i in range(len(G.V)):
        for edge in G.E:
            relax(edge)
    for edge in G.E:
        u=edge.startv
        v=edge.endv
        w=edge.w
        newDist=u.d+w
        if v.d>newDist:
            return False#sadrzi negativne tezine
    return True
#----------------------------------------------
def ShortestPath(G, nodeA, nodeB):
    nesto=Bellman(G, nodeA)
    temp=nodeB
    path=[]
    while temp is not None:
        path.append(temp.name)
        temp=temp.p
    path.reverse()
    return (path, nodeB.d)
#----------------------------------------------
def UpdateEdge(G, nodeA, nodeB, weight):
    exists=False
    for edge in G.E:
        if edge.startv.name==nodeA.name and edge.endv.name==nodeB.name:
            edge.w=weight
            exists=True
    if exists==False:
        G.E.append(Edge(nodeA, nodeB, weight))
G=MakeGraph()
indeglist=GetInDeg(G)
outdeglist=GetOutDeg(G)
print("Input degrees list:", indeglist, "\nOutput degrees list:", outdeglist)
for i in G.V:
    if i.name=="a":
        nodeA=i
    if i.name=="e":
        nodeB=i
(path, dist)=ShortestPath(G, nodeA, nodeB)
print("Najkraca putanja od", nodeA.name, "do", nodeB.name, "je", dist, "i ide preko cvorova", path)
copyG=G
for i in G.V:
    if i.name=="b":
        b=i
    if i.name=="c":
        c=i
UpdateEdge(copyG, b, c, -4)
#for edge in copyG.E:
    #print("(", edge.startv.name, ",", edge.endv.name, ")=", edge.w)
(path, dist)=ShortestPath(copyG, nodeA, nodeB)
print("Nova najkraca putanja od", nodeA.name, "do", nodeB.name, "je", dist, "i ide preko cvorova", path)