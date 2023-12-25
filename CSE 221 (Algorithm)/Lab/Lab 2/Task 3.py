def task(arr):
   res=[]
   def sort2nd(arr):
       return arr[1]
   arr=sorted(arr,key=sort2nd)
   res.append(arr[0])
   c=1
   m=0
   for i in range(1,len(arr)):
       if arr[i][1]>=arr[m][1]:
          res.append(arr[i])
          c+=1
          m=i
   return c,res

c=1
while(c<4):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/input3_si{c}.txt','r')
  n=int(input.readline())
  a1=[]
  for i in range(n):
    s=input.readline()
    ss=s.split(' ')
    a=[]
    a.append(int(ss[0]))
    a.append(int(ss[1]))
    a1.append(a)

  m,n=task(a1)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 2/output3_so{c}.txt','w')
  for i in range(len(n)):
    if i!=len(n)-1:
      output.write(f'{n[0]} {n[1]}\n')
    else:
      output.write(f'{n[0]} {n[1]}')
  output.close()
  c+=1