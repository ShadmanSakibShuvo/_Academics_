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

def result(G,n,cl):
    visited,p=[False]*(n+1),[False]*(n+1)
    stack=[]
    for node in range(1,n+1):
        if not visited[node]:
            result=dfs(G,node,visited,stack,p)
            if result=="IMPOSSIBLE":
                return "IMPOSSIBLE"
    result,c=[],0
    while c<len(cl):
        if not cl[c][0] in result:
            result.append(cl[c][0])
        if not cl[c][1] in result:
            result.append(cl[c][1])
        c=cl[c][1]
    return result
    

c=1
while c<3:
    input=open(f'input2_{c}.txt', 'r')
    nm=input.readline()
    nms=nm.split(' ')
    n,m=int(nms[0]),int(nms[1]) 

    prereq,s,e=[],None,None
    for i in range(m):
        s=input.readline()
        ss=s.split()
        prereq.append((int(ss[0]),int(ss[1])))
        if i==1:
            s=int(ss[0])
        if i==m-1:
            e=int(ss[1])
    
    G = {i:[] for i in range(1,n+1)}
    cl=[]
    for pre in prereq:
        A,B,cll=pre[0],pre[1],[]
        cll.append(A)
        cll.append(B)
        cl.append(cll)
        G[A].append(B)
    
    res2=result(G,n,cl)
    print(res2)

    output=open(f'output2_{c}.txt', 'w')
    for i in range(len(res2)):
        output.write(f'{res2[i]} ')     
    output.close()
    c+=1