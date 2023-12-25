def merge(a, b):
    result=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    result+=a[i:]
    result+=b[j:]
    return result

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

c=1
while(c<5):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/Task 1_si{c}.txt','r')
  n=int(input.readline())
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(n):
    arr.append(int(ss[i]))

  l=mergeSort(arr)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/output 1_so{c}.txt','w')
  for i in range(len(l)):
    if i!=len(l)-1:
      output.write(f'{l[i]} ')
    else:
      output.write(f'{l[i]}')
  output.close()
  c+=1