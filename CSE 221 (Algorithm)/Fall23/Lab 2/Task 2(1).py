def add(N,M):
  l=[]
  for i in range(len(N)):
    l.append(N[i])
  for i in range(len(M)):
    l.append(M[i])
  l.sort()
  return l

c=1
while(c<5):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/input2_si{c}.txt','r')
  n=int(input.readline())
  a1=[]
  s=input.readline()
  ss=s.split(' ')
  for i in range(n):
    a1.append(int(ss[i]))
  n2=int(input.readline())
  a2=[]
  s=input.readline()
  ss=s.split(' ')
  for i in range(n2):
    a2.append(int(ss[i]))

  l=add(a1,a2)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/output2_so{c}.txt','w')
  for i in range(len(l)):
    if i!=len(l)-1:
      output.write(f'{l[i]} ')
    else:
      output.write(f'{l[i]}')
  output.close()
  c+=1