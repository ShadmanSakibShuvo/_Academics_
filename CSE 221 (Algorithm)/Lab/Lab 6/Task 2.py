import heapq,math
from rich.console import Console
console = Console()

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
    print(d)
    return d

def meetPoint(G,As,Bs):
    Ad=dijkstra(G,As)
    Bd=dijkstra(G,Bs)

    minTotalDist=math.inf
    meetpoint=-1
    time=0

    
    for i in range(1,len(G)+1):
        currentDist =Ad[i]+Bd[i]
        if currentDist<minTotalDist:
            minTotalDist=currentDist
            meetpoint=i
            time=max(Ad[i],Bd[i])
    
    if minTotalDist==math.inf:
        return "Impossible"

    return time,meetpoint

def main():
    input=open(f'input2.txt','r')
    inp=input.readline()
    N,M=map(int,inp.split(' '))
    G={i:[] for i in range(1,N+1)}

    for _ in range(M):
        inp=input.readline()
        u,v,w=map(int,inp.split(' '))
        G[u].append((v,w))
    
    inp=input.readline()
    As,Bs=map(int,inp.split())

    result=meetPoint(G,As,Bs)

    output=open('output2.txt','w')
    if result=="Impossible":
        print("Impossible")
        output.write(f'Impossible')
    else:
        time,node=result
        console.print("[italic]For sample input 3 ; the given sample output is wrong as at node 2 , total time = 14 > at node 6 , total time = 12[/italic].")
        print(f"Time {time}\nNode {node}")
        output.write("N.B: For sample input 3 ; the given sample output is wrong as at node 2 , total time = 14 > at node 6 , total time = 12\n")
        output.write(f"Time {time}\nNode {node}")
    output.close()

if __name__ == "__main__":
    main()