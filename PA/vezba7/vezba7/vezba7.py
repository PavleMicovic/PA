class Data:
    def __init__(self, key=None, literal=None):
        self.key=key
        self.literal=literal
def h(k, m):
    return k%m

def hash(k,i,m):
    return(h(k,m)+i)%m

def chained_hash_insert(T,x,m):
    if(x.literal not in T[h(x.key,m)]):
        T[h(x.key, m)].insert(0,x.literal)

def chained_hash_search(T,k, m):
    for i in range (len(T[h(k.literal,m)])):
        if T[h(k.literal,m)][i]==k.literal:
            return i
def chained_hash_delete(T,x,m):
    T[h(x.key,m)].remove(x.literal)
def hash_insert(T,k,m):
    if(k.literal not in T):
        for i in range(m+1):
            j=hash(k.key,i,m)
            if(T[j]==None or T[j]=='D'):
                T[j]=k.literal
                return j
            else:
                i+=1
        print("Error hash table overflow")
def hash_search(T,k,m):
    i=0
    j=hash(k.key,i,m)
    while(T[j]!=None and i!=m):
        j=hash(k.key,i,m)
        if(T[j]==k.literal):
            return j
        i+=1
    return None
def hash_delete(T, k,m):
    i=hash_search(T,k,m)
    T[i]='D'
a=Data(1,1)
b=Data(2,2)
c=Data(3,3)
d=Data(1,6)
T=[]
m=10
for i in range(m):
    T.append(None)
#for i in range(m):
#    T.append([])
#chained_hash_insert(T,a,m)
#chained_hash_insert(T,a,m)
#chained_hash_insert(T,a,m)
#print(T)
#chained_hash_insert(T,b,m)
#print(T)
#chained_hash_insert(T,c,m)
#print(T)
#chained_hash_insert(T,d,m)
#print(T)

#print(chained_hash_search(T,a,m))

#chained_hash_delete(T,a,m)
#print(T)

hash_insert(T, a, m)
#print(T)
hash_insert(T, b, m)
#print(T)
hash_insert(T, c, m)
#print(T)
hash_insert(T, d, m)
print(T)

print("Element 6 se nalazi na ", hash_search(T,d,m), "poziciji\n")
hash_delete(T,a,m)
print("Obrisali smo element 1:\n", T,"\n")
hash_delete(T,d,m)
print("Obrisali smo element 6:\n", T,"\n")
hash_insert(T, d, m)
hash_insert(T, a, m)
print(T)