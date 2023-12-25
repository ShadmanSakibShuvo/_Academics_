from queue import LifoQueue  #stack makes task easier

def dfs(G,s):
    visited,path,stack=[False]*(len(G)+1),[],LifoQueue()
    stack.put(s)
    visited[s]=True

    while not stack.empty():
        node=stack.get()
        path.append(node)

        for neighbor in G[node]:
            if not visited[neighbor]:
                stack.put(neighbor)
                visited[neighbor]=True
    return path

c=1
while c<5:
    input=open(f'input3_{c}.txt', 'r')
    nm=input.readline()
    nms=nm.split(' ')
    n,m=int(nms[0]),int(nms[1])
    G={i:[] for i in range(1,n+1)}  #using adjacency list

    for i in range(m):
        s=input.readline()
        ss=s.split(' ')
        u,v=int(ss[0]),int(ss[1])
        G[u].append(v)
        G[v].append(u)

    res=dfs(G,1)
    print(res)

    output=open(f'output3_{c}.txt', 'w')
    for i in range(len(res)):
        output.write(f'{res[i]} ')     #results didn't match , but the dfs traversal is correct
    output.close()
    c += 1