n=int(input())
b=0
for i in range(0,n,1):
    s=input()
    ss=s.replace(" ","")
    l=[]
    for i in ss:
        if (i=="1"):
            l.append(i)
    m=len(l)
    if (m>=2):
        b+=1 
print(b)