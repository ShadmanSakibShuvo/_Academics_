def rightRotate(l):
    t=l[len(l)-1]
    for i in range((len(l)-1),0,-1):
      l[i]=l[i-1]
    l[0]=t
    return l

n=int(input())
s=input()
ss=s.split(' ')
l=[]
for i in range(0,len(ss)):
    l.append(int(ss[i]))

for i in range(0,n):
   m=rightRotate(l)

print(m)
