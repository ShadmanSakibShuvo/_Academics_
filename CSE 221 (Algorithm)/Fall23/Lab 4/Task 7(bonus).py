from queue import Queue

def bfs(G,s):
    visited=set()
    queue=Queue()
    queue.put((s, 0))
    fnode,mdistance=s,0

    while not queue.empty():
        curr,distance=queue.get()
        if distance>mdistance:
            mdistance=distance
            fnode=curr
        visited.add(curr)
        for neighbor in G[curr]:
            if neighbor not in visited:
                queue.put((neighbor,distance+1))
    return fnode,mdistance

def farthestCities(n,G):
    farthest1,_=bfs(G, 1)
    farthest2,_= bfs(G,farthest1)
    return farthest1,farthest2

c=1
while c<4:
    input=open(f'input7_{c}.txt', 'r')
    n=input.readline()
    nn=int(n[0])
    G={i:[]for i in range(1,nn+1)}     #using adjacency list

    s=input.readline()
    ss=s.split(' ') 
    u,v=int(ss[0]),int(ss[1])
    if u not in G:
        G[u]=[]
    if v not in G:
        G[v]=[]
    G[u].append(v)
    G[v].append(u)

    res=farthestCities(nn,G)

    output=open(f'output7_{c}.txt', 'w')
    output.write(f'{res[0]} {res[1]}')
    output.close()
    c+=1