from collections import defaultdict,deque

def dfs(G,node,visited,stack):
    visited[node]=True
    for neighbor in G[node]:
        if not visited[neighbor]:
            dfs(G,neighbor,visited,stack)
    stack.append(node)

def transpose(G):
    transposed=defaultdict(list)
    for node in G:
        for neighbor in G[node]:
            transposed[neighbor].append(node)
    return transposed

def dfsGt(G,node,visited,component):
    visited[node]=True
    component.append(node)
    for neighbor in G[node]:
        if not visited[neighbor]:
            dfsGt(G,neighbor,visited,component)

def scc(G,Gt,vis):
    visited={vi:False for vi in vis}
    stack=deque()
    for vi in vis:
        if not visited[vi]:
            dfs(G,vi,visited,stack)
    visited={vi:False for vi in vis}
    sccl=[]
    while stack:
        vi=stack.pop()
        if not visited[vi]:
            component=[]
            dfsGt(Gt,vi,visited,component)
            sccl.append(sorted(component))
    return sccl

def main():
    c=1
    while c<4:
        input=open(f'input3_{c}.txt', 'r')
        nm=input.readline()
        nms=nm.split(' ')
        n,m=int(nms[0]),int(nms[1])
        G=defaultdict(list)
        for _ in range(m):
            uv=input.readline()
            u,v=map(int,uv.split())
            G[u].append(v)

        Gt=transpose(G)
        vi=set(range(1, n+1))
        sccl=scc(G,Gt,vi)

        output=open(f'output3_{c}.txt', 'w')
        for component in sorted(sccl):
            for i in component:
                output.write(f'{i} ')
            output.write('\n')
            print(component)

        print('\n')
        c+=1
if __name__ == "__main__":
    main()
