def diff(n,arr):
  for i in range(0,len(arr)):
    for j in range(i,len(arr)):
      if n==(arr[i]+arr[j]) and i!=j:
        return i+1,j+1
  return f'IMPOSSIBLE',None

c=1
while(c<5):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/input1_si{c}.txt','r')
  n=input.readline()
  ns=n.split(' ')
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(int(ns[0])):
    arr.append(int(ss[i]))

  o,p=diff(int(ns[1]),arr)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/output1_so{c}.txt','w')
  if(p!=None):
    output.write(f'{o} {p}')
  else:
    output.write(f'{o}')
  output.close()
  c+=1