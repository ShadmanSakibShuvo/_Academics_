def count(arr):
    if len(arr)<=1:
        return arr, 0
    mid=len(arr)//2
    left,invleft=count(arr[:mid])
    right,invright=count(arr[mid:])
    merged,invcount=merge(left,right)
    return merged,invcount+invleft+invright

def merge(a1,a2):
    result=[]
    invcount=0
    i=j=0
    while i<len(a1) and j<len(a2):
        if a1[i]<=a2[j]:
            result.append(a1[i])
            i+=1
        else:
            result.append(a2[j])
            j+=1
            invcount+=len(a1)-i
    result+=a1[i:]
    result+=a2[j:]
    return result,invcount


c=1
while(c<4):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/Task 3_si{c}.txt','r')
  n=int(input.readline())
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(n):
    arr.append(int(ss[i]))

  m,n=count(arr)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/output 3_so{c}.txt','w')
  output.write(str(n))
  output.close()
  c+=1