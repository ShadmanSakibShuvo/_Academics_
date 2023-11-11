n=int(input())
for i in range(0,n,1):
    s=input()
    a=len(s)
    if (a<=10):
        print(s)
    else:
        last=s[-1]
        first=s[0:1]
        aa=a-2
        print(first+str(aa)+last)