from enum import Enum
import queue
import math	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d = None, f = None, connections=None, name=None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.color = c
        self.p = p
        self.d = d
        self.f = f
        self.connections=connections
        self.name=name

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255
        		
def susedi(cvor):
    print("Susedi cvora ", cvor.name, ":\n")
    for i in range(len(cvor.connections)):
        print(cvor.connections[i].name)
    print("---------------------------------\n")

def veze(cvor):
    print("Veze cvora", cvor.name, ":\n")
    for i in range (len(cvor.connections)):
        print("E(", cvor.name,", ", cvor.connections[i].name,")\n")

def add_to_list(cvor, sused):
    cvor.connections.append(sused)
def BFS(G, s):
    for i in range(len(G)):
        G[i].color=VertexColor.WHITE
        G[i].d=math.inf
        G[i].p=None
    s.color=VertexColor.GRAY
    s.d=0
    s.p=None
    #print("Ime cvora preko kojeg trazimo:", s.name)
    Q=queue.Queue()
    Q.put(s)
    #print("Cvor iz reda:", Q.get().name)
    while(Q.empty()==False):
        u=Q.get()
        for i in u.connections:
            #print("Boja ovog", i.color)
            if i.color==VertexColor.WHITE:
                i.color=VertexColor.GRAY
                i.d=u.d+1
                i.p=u
                #print("Cvor koji obradjujemo:", i.name, "Cvor koji je njegov parent:", i.p.name)
                Q.put(i)
            u.color=VertexColor.BLACK
def print_path(G, s, v):
    if v==s:
        print(s.name)
    elif v.p==None:
        print("No path from", s.name, "to", v.name, "exists")
    else:
        print_path(G, s, v.p)
        print(v.name)
time=None
l=[]
def DFS(G):
    global time
    global l
    for i in G:
        i.color=VertexColor.WHITE
        i.p=None
    time=0
    for i in G:
        if(i.color==VertexColor.WHITE):
            DFS_visit(G, i)
def DFS_visit(G, u):
    global time
    global l
    time=time+1
    u.d=time
    u.color=VertexColor.GRAY
    for i in u.connections:
        if i.color==VertexColor.WHITE:
            i.p=u
            DFS_visit(G, i)
    u.color=VertexColor.BLACK
    time=time+1
    u.f=time
    l.append(u)
v1 = Vertex(connections=[], name=1)
v2 = Vertex(connections=[], name=2)
v3=Vertex(name=3, connections=[])
v4=Vertex(name=4, connections=[])
v5=Vertex(name=5, connections=[])
#cvor 1:
add_to_list(v1, v2)
add_to_list(v1, v5)
#-----------------------------------
#cvor 2:
add_to_list(v2, v1)
add_to_list(v2, v5)
add_to_list(v2, v4)
add_to_list(v2, v3)
#-----------------------------------
#cvor 3:
add_to_list(v3, v2)
add_to_list(v3, v4)
#-----------------------------------
#cvor 4:
add_to_list(v4, v2)
add_to_list(v4, v5)
add_to_list(v4, v3)
#-----------------------------------
#cvor 5:
add_to_list(v5, v1)
add_to_list(v5, v2)
add_to_list(v5, v4)
#-----------------------------------
#susedi(u)
#veze(u)
#susedi(v)
#veze(v)
#susedi(v3)
#veze(v3)
#veze(v2)
#G=[v1, v2, v3, v4, v5]
#BFS(G, v3)
#print("Putanja od 3 do 1:")
#print_path(G, v3, v1)
#print("\nPutanja od 3 do 5:")
#print_path(G, v3, v5)

#----------------------------------------------------
v_ushorts = Vertex(connections=[], name="undershorts")
v_pants = Vertex(connections=[], name="pants")
v_belt=Vertex(name="belt", connections=[])
v_socks=Vertex(name="socks", connections=[])
v_shoes=Vertex(name="shoes", connections=[])
v_watch=Vertex(name="watch", connections=[])
v_shirt=Vertex(name="shirt", connections=[])
v_tie=Vertex(name="tie", connections=[])
v_jacket=Vertex(name="jacket", connections=[])


add_to_list(v_ushorts, v_pants)
add_to_list(v_ushorts, v_shoes)

add_to_list(v_pants, v_belt)
add_to_list(v_pants, v_shoes)


add_to_list(v_belt, v_jacket)

add_to_list(v_shirt, v_belt)
add_to_list(v_shirt, v_tie)

add_to_list(v_tie, v_jacket)

add_to_list(v_socks, v_shoes)

G1=[v_shirt, v_tie, v_jacket, v_belt, v_watch, v_ushorts, v_pants, v_shoes, v_socks]
#veze(v_ushorts)
#veze(v_belt)
#veze(v_shirt)
#veze(v_tie)
#veze(v_jacket)
#veze(v_socks)
#veze(v_shoes)
#veze(v_watch)

DFS(G1)
l.reverse()
for i in l:
    if i.p!=None: 
        a=i.p.name 
    else: 
        a=i.p
    print(i.name, ", ", i.f, ", ", i.d, ", ", a)










