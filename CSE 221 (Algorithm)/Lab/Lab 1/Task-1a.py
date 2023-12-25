def evenOdd(n):
  if(n%2==0):
    return f'{n} is an Even number.'
  else:
    return f'{n} is an Odd number'

input=open('/content/drive/MyDrive/221 lab input files/Lab 1/input1a.txt','r')
t=int(input.readline())
output=open('/content/drive/MyDrive/221 lab input files/Lab 1/output1a.txt','w')
for i in range(0,t):
  k=int(input.readline())
  m=evenOdd(k)
  output.write(m)
  if(i==t-1):
    continue
  output.write('\n')
output.close()