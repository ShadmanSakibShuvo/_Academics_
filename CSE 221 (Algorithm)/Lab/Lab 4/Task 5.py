from queue import Queue

def bfsSP(G,s,e):
    queue=Queue()
    queue.put((s,[s]))
    visited=set()

    while not queue.empty():
        c,path=queue.get()
        if c==e:
            return path
        if c not in visited:
            visited.add(c)
            for neighbor in G[c]:
                queue.put((neighbor,path+[neighbor]))
    return None

c=1
while c<6:
    input=open(f'input5_{c}.txt', 'r')
    nmd=input.readline()
    nmds=nmd.split(' ')
    n,m,d=int(nmds[0]),int(nmds[1]),int(nmds[2])
    G={i:[]for i in range(1,n+1)}     #using adjacency list
  
    for i in range(m):
        s=input.readline()
        ss=s.split(' ')
        u,v=int(ss[0]),int(ss[1])
        G[u].append(v)
        G[v].append(u)


    res=bfsSP(G,1,d)
    print(res,end='\n')

    output=open(f'output5_{c}.txt', 'w')
    output.write(f'Time: {len(res)-1}\nShortest Path: ')
    for i in range(len(res)):
        output.write(f'{res[i]} ')
    output.close()
    c+=1