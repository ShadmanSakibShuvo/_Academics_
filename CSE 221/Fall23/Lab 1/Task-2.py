def bubbleSort(arr):
  for i in range(len(arr)-1):
    bool='False'
    for j in range(len(arr)-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        bool='True'
    if(bool=='False'):
      break
  return arr


input=open('/content/drive/MyDrive/221 lab input files/Lab 1/input2.txt','r')
t=int(input.readline())
arr=[]
s=input.readline()
s1=s.split(' ')
output=open('/content/drive/MyDrive/221 lab input files/Lab 1/output2.txt','w')
for i in range (0,len(s1)):
  arr.append(int(s1[i]))
o=bubbleSort(arr)
for i in range(0,len(o)):
  output.write(str(o[i]))
  output.write(' ')
output.close()