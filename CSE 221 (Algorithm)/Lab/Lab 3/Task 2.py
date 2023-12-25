def max(arr):
    if len(arr)==1:
        return arr[0]
    else:
        mid=len(arr)//2
        max1=max(arr[:mid])
        max2=max(arr[mid:])
        if max1>max2:
          return max1
        else:
          return max2

c=1
while(c<5):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/Task 2_si{c}.txt','r')
  n=int(input.readline())
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(n):
    arr.append(int(ss[i]))

  m=max(arr)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/output 2_so{c}.txt','w')
  output.write(str(m))
  output.close()
  c+=1