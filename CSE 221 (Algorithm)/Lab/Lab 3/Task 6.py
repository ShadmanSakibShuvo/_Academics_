def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high

    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1

        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break

    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_select(arr,low,high,k):
    if low<=high:
        pivot_index=partition(arr,low,high)
        if pivot_index==k-1:
            return arr[pivot_index]
        elif pivot_index>k-1:
            return quick_select(arr,low,pivot_index-1,k)
        else:
            return quick_select(arr,pivot_index+1,high,k)
    return None

c=1
while(c<2):
  input=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/Task 6.txt','r')
  n=int(input.readline())
  s=input.readline()
  ss=s.split(' ')
  arr=[]
  for i in range(n):
    arr.append(int(ss[i]))

  output=open(f'/content/drive/MyDrive/221 lab input files/Lab 3/output 6.txt','w')

  n2=int(input.readline())
  for i in range(n2):
      k=int(input.readline())
      rarr=quick_select(arr,0,n-1,k)
      output.write(f'{rarr}\n')
  output.close()
  c+=1