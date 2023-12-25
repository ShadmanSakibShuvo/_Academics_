def op(n1,operator,n2):
  if(operator=='+'):
    return n1+n2
  elif operator=='-':
    return n1-n2
  elif operator=='*':
    return n1*n2
  else:
    return n1/n2

input=open('/content/drive/MyDrive/221 lab input files/Lab 1/input1b.txt','r')
t=int(input.readline())
output=open('/content/drive/MyDrive/221 lab input files/Lab 1/output1b.txt','w')
for i in range(0,t):
  s=input.readline()
  s1=s.split(' ')
  n1=int(s1[1])
  n2=int(s1[3])
  operator=s1[2]
  k=op(n1,operator,n2)
  k1=f'The result of {n1} {operator} {n2} is {k}'
  output.write(k1)
  if(i==t-1):
    continue
  output.write('\n')
output.close()