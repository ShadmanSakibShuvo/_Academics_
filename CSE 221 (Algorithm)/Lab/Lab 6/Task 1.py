import heapq,math

def dijkstra(G,S):
    d={v:math.inf for v in G}
    p={v:None for v in G}
    d[S]=0
    q=[(0,S)]
    while q:
        cd,cv=heapq.heappop(q)
        if cd>d[cv]:
            continue
        for n,w in G[cv]:
            dThroughc=cd+w
            if dThroughc<d[n]:
                d[n]=dThroughc
                p[n]=cv
                heapq.heappush(q,(dThroughc,n))
    return d

def main():
    input=open(f'input1.txt','r')
    inp=input.readline()
    N,M=map(int,inp.split(' '))
    G={i:[] for i in range(1,N+1)}

    for _ in range(M):
        inp=input.readline()
        u,v,w=map(int,inp.split(' '))
        G[u].append((v,w))
        
    inp=input.readline()
    s=int(inp)

    ds= dijkstra(G,s)

    output=open('output1.txt','w')
    for i in range(1,N+1):
        if ds[i]==math.inf:
            print(-1,end=" ")
            output.write(f'-1 ')
        else:
            print(ds[i],end=" ")
            output.write(f'{ds[i]} ')
    if output:
        output.close()
if __name__ == "__main__":
    main()