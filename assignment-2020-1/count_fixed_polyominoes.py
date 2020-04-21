import sys,pprint
if (len(sys.argv)==3):
    input1=sys.argv[1]
    input2=sys.argv[2]
if(len(sys.argv)==2):
    input2=sys.argv[1]
    input1=None
#μετατροπη string-->int
n=int(input2)
g={}
for y in range(n):
    for x in range (-(n-2),n):
        if y==0 and x<0:
            continue
        if abs(x) + y > n-1:
            continue
        g[x,y]=[]
#Δημιουργία κλειδι΄΄ων
for y in range(n):
    for x in range (-(n-2),n):
        #Αν το y είναι 0 το χ πρέπει να ναι θετικό
        if y==0 and x<0:
            continue
        if abs(x) + y > n-1:
            continue
            #Να δω αν βολέυει να γίνει set αντι για list
        if (x+1,y) in g:
            g[x,y].append((x+1,y))
        if (x,y+1) in g:
            g[x,y].append((x,y+1))
        if (x-1,y) in g:
            g[x,y].append((x-1,y))
        if (x,y-1) in g:
            g[x,y].append((x,y-1))
#Αρχικοποίηση untried σαν set
untried={(0,0)}
#Αρχικοποίηση p=current polyomino σαν list
p=[]
#Αρχικοποίηση global μεταβλητής
c=0
#Αυξηση global μεταβλητης c κατα 1
def AddOne():
    global c
    c=c+1
def Neigbors(p,u,v):
    l=p.copy()
    l.remove(u)
    x=[value for value in g[v] if value in l]
    if len(x)==0:
        return True
    else:
        return False
#Αρχή Μεθόδου
def CountFixedPolyominoes(g,untried,n,p,c):
    while len(untried)>0:
        u=untried.pop()
        p.append(u)
        if len(p)==n:
            AddOne()
        else:
            new_neigbors=set()
            for v in g[u]:
                if v not in untried and v not in p and Neigbors(p,u,v):
                    new_neigbors.add(v)
            new_untried=set()
            if len(untried)>0:
                new_untried.update (untried)
            new_untried.update(new_neigbors)
            CountFixedPolyominoes(g,new_untried,n,p,c)
        p.pop()
CountFixedPolyominoes(g,untried,n,p,c)
if input1=="-p":
    pprint.pprint(g)
print(c)
