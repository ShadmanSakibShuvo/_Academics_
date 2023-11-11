ss=input()
ss1=ss.split(" ")
n=int(ss1[0])
m=int(ss1[1])
a=int(ss1[2])
s1=n//a 
if (n%a!=0):
    s1+=1 
s2=m//a 
if (m%a!=0):
    s2+=1 
s=s1*s2
print(s)