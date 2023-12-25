from queue import Queue     #make tasks easier

def dfs(G,node,visited,stack,p):
    visited[node],p[node]=True,True

    for neighbor in G[node]:
        if not visited[neighbor]:
            if dfs(G,neighbor,visited,stack,p)=="IMPOSSIBLE":
                return "IMPOSSIBLE"
        elif p[neighbor]:
            return "IMPOSSIBLE"
    p[node]=False
    stack.append(node)
    return stack

def topoSort(G,N):
    visited,p=[False]*(N+1),[False]*(N + 1)
    stack=[]
    for node in range(1,N+1):
        if not visited[node]:
            result=dfs(G,node,visited,stack,p)
            if result=="IMPOSSIBLE":
                return "IMPOSSIBLE"
    return result[::-1] if len(result) == N else "IMPOSSIBLE"


def courseOrderDFS(N, prereq):
    G = {i:[] for i in range(1,N+1)}
    for pre in prereq:
        A,B=pre
        G[A].append(B)
    order=topoSort(G,N)
    return order






def courseOrderBFS(N,prereq):
    G = {i:[] for i in range(1,N+1)}    #using adjacency list
    indegree=[0]*(N+1)

    for a,b in prereq:
        G[a].append(b)
        indegree[b]+=1

    queue=Queue()
    for i in range(1,N+1):
        if indegree[i]==0:
            queue.put(i)

    path=[]

    while not queue.empty():
        node=queue.get()
        path.append(node)
        for neighbor in G[node]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                queue.put(neighbor)

    if len(path)!=N:
        return "IMPOSSIBLE"
    return path






c=1
while c<4:
    input=open(f'input1_{c}.txt', 'r')
    nm=input.readline()
    nms=nm.split(' ')
    n,m=int(nms[0]),int(nms[1]) 

    prereq=[]
    for _ in range(m):
        s=input.readline()
        A,B=map(int,s.split())
        prereq.append((A,B))

    res1=courseOrderDFS(n,prereq)
    print(res1)

    output=open(f'output1a_{c}.txt', 'w')
    for i in range(len(res1)):
        output.write(f'{res1[i]} ')     
    output.close()

    res2=courseOrderBFS(n,prereq)
    print(res2)

    output=open(f'output1b_{c}.txt', 'w')
    for i in range(len(res2)):
        output.write(f'{res2[i]} ')     
    output.close()
    c += 1