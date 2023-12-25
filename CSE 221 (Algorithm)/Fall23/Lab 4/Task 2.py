from queue import Queue     #make tasks easier

def bfs(G,s):
    visited,path,queue=[False]*(len(G)+1),[],Queue()
    queue.put(s)
    visited[s]=True

    while not queue.empty():
        node=queue.get()
        path.append(node)
        for neighbor in G[node]:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor]=True
    return path

c=1
while(c<5):
  input=open(f'input2_{c}.txt','r')
  nm=input.readline()
  nms=nm.split(' ')
  n,m=int(nms[0]),int(nms[1])
  G={i:[]for i in range(1,n+1)}     #using adjacency list
  
  for i in range(m):
    s=input.readline()
    ss=s.split(' ')
    u,v=int(ss[0]),int(ss[1])
    G[u].append(v)
    G[v].append(u)

  res=bfs(G,1)
  print(res,end='\n')

  output=open(f'output2_{c}.txt','w')
  for i in range(len(res)):
     output.write(f'{res[i]} ')
  output.close()
  c+=1