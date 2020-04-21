import sys,pprint
from collections import deque
input1=sys.argv[1]
if(len(sys.argv)==5):
    txt=str(sys.argv[4])
    radius=str(sys.argv[2])
else:
    txt=str(sys.argv[3])
    radius=None
g = {}
with open(txt) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        g[nodes[1]].append(nodes[0])
    nodes = g.keys()
    num_nodes = len(nodes)
def findci(g, node):
    q =deque()
    update=[]
    sentinel =num_nodes+1
    i=0
    rneigbors=0
    visited = [ False ] * int(num_nodes+1)
    inqueue = [ False ] * int(num_nodes+1)
    inqueue[node] = True
    q.appendleft(node)
    q.appendleft(sentinel)
    while not (len(q) == 1 or i==int(radius)+2):
        #print("Queue", q)
        c = q.pop()
        if c == sentinel:
            i += 1
            q.appendleft(sentinel)
            continue
        #print("Visiting", c,i)
        inqueue[c] = False
        visited[c] = True
        if c!=node and node not in update:
            update.append(c)
        if i==int(radius):
            rneigbors=rneigbors + (len(g[c])-1)
        for v in g[c]:
            #print("VV",v)
            if not visited[v] and not inqueue[v]:
                q.appendleft(v)
                inqueue[v] = True
    return((len(g[node])-1)*int(rneigbors),update)
if input1=="-c":
    for k in range(int(sys.argv[2])):
        max=-1
        vmax=len(g)+1
        for v in g:
            if len(g[v])>max:
                max=len(g[v])
                vmax=v
            if len(g[v])==max and v<vmax:
                max=len(g[v])
                vmax=v
        print(vmax,max)
        g.pop(vmax)
        for v in g:
            for k in g[v]:
                if k==vmax:
                    g[v].remove(vmax)
else:
    max=-1
    vmax=len(g)+1
    ci={}
    nnodes={}
    for v in g:
        (ci[v],nnodes[v])=findci(g,v)
        if ci[v]>max:
            max=ci[v]
            vmax=v
        if ci[v]==max and v<vmax:
            max=ci[v]
            vmax=v
    print(vmax,max)
    ci[vmax]=-10
    g.pop(vmax)
    for v in g:
        for k in g[v]:
            if k==vmax:
                g[v].remove(vmax)
    for k in range(int(sys.argv[3])-1):
        for m in nnodes[vmax]:
            (ci[m],nnodes[m])=findci(g,m)
        max=-1
        vmax=len(g)+1
        for v in g:
            if ci[v]>max:
                max=ci[v]
                vmax=v
            if ci[v]==max and v<vmax:
                max=ci[v]
                vmax=v
        print(vmax,max)
        ci[vmax]=-10
        g.pop(vmax)
        for v in g:
            for k in g[v]:
                if k==vmax:
                    g[v].remove(vmax)
