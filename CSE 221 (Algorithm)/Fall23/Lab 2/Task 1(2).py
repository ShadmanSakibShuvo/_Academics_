def diff2(n,arr):
  i=0
  j=len(arr)-1
  while i<=j and j>-1 and i!=j:
    sum=arr[i]+arr[j]
    if sum==n:
      return i+1,j+1
      break
    else:
      if sum>n:
        j-=1
      if sum<n:
        i+=1
  return f'Impossible',None

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

  o,p=diff2(int(ns[1]),arr)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/output1_so{c}.txt','w')
  if(p!=None):
    output.write(f'{o} {p}')
  else:
    output.write(f'{o}')
  output.close()
  c+=1