ss=input()
ss1=ss.split(" ")
n=int(ss1[0])
k=int(ss1[1])
 
ss2=input()
ss12=ss2.split(" ")
l=len(ss12)
a=[]
for i in range(0,l):
    a.append(int(ss12[i]))
 
 
l2=len(a)
x=0
y=a[k-1]
for i in range(0,l2):
    if(a[i]>=y and a[i]>0 and a[i]<101):
        #print(a[i])
        x+=1
print(x)