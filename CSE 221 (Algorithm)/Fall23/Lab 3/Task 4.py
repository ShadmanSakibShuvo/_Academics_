def msquared(arr):
    if len(arr)==1:
        return arr[0]  #as 1 <= i < j <= N
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    ml=msquared(left)
    mr=msquared(right)
    mc1=max(left)+max(right)**2
    mc2=max(left)+min(right)**2
    if(mc1>mc2):
      mc=mc1
    else:
      mc=mc2
    if ml>mr and ml>mc:
      return ml
    elif mr>ml and mr>mc:
      return mr
    else:
      return mc



c=1
while(c<4):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/Task 4_si{c}.txt','r')
  n=int(input.readline())
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(n):
    arr.append(int(ss[i]))

  m=msquared(arr)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/output 4_so{c}.txt','w')
  output.write(str(m))
  output.close()
  c+=1