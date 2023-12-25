import numpy as np
def adjacencyMatx(res,ui,vi,wi):
    res[ui][vi]=wi
    return res

c=1
while(c<3):
  input=open(f'input1a_{c}.txt','r')
  nm=input.readline()
  nms=nm.split(' ')
  n,m=int(nms[0]),int(nms[1])
  res=np.zeros((int(n+1),int(n+1)),dtype=int)
  
  for i in range(m):
    s=input.readline()
    ss=s.split(' ')
    res=adjacencyMatx(res,int(ss[0]),int(ss[1]),int(ss[2]))

  print(res)
  output=open(f'output1a_{c}.txt','w')
  output.write(str(res))
  output.close()
  c+=1