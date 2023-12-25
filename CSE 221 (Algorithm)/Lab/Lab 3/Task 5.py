def quicksort(a,p,r):
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

c=1
while(c<5):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/Task 5_si{c}.txt','r')
  n=int(input.readline())
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(n):
    arr.append(int(ss[i]))

  quicksort(arr,0,n-1)

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/output 5_so{c}.txt','w')
  output.write(' '.join(map(str,arr)))
  output.close()
  c+=1