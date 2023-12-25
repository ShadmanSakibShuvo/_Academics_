def cycle(G,visited,c,stack):
    visited[c],stack[c]=True,True

    for neighbor in G[c]:
        if not visited[neighbor]:
            if cycle(G,visited,neighbor,stack):
                return True
        elif stack[neighbor]:
            return True

    stack[c]=False
    return False

def checkCycle(n,uis):
    G={i:[] for i in range(1,n+1)}       #using adjacency list
    for ui in uis:
        G[ui[0]].append(ui[1])
    visited={i:False for i in range(1,n+1)}
    stack={i:False for i in range(1,n+1)}

    for node in G:
        if not visited[node]:
            if cycle(G,visited,node,stack):
                return "YES"
    return "NO"

c=1
while c<6:
    input=open(f'input4_{c}.txt', 'r')
    nm=input.readline()
    nms=nm.split(' ')
    n,m=int(nms[0]),int(nms[1]) 

    edges=[]
    for i in range(m):
        s=input.readline()
        ss=s.split(' ')
        u,v=int(ss[0]),int(ss[1])
        edges.append((u,v))

    res=checkCycle(n,edges)
    print(res)

    output=open(f'output4_{c}.txt', 'w')
    output.write(res)
    output.close()
    c += 1



