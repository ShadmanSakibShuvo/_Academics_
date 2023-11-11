def arrival(n):
    s=input()
    s1=s.split(" ")
    ss=[]
    for i in range(0,len(s1)):   #can be shortened by using int seperately without using a loop
        ss.append(int(s1[i]))
    mx=ss[0]
    mxp=0
    mn=ss[0]
    mnp=0
    for i in range(0,len(ss)):
        if(ss[i]>mx):
            mx=ss[i]
            mxp=i
        if(ss[i]<=mn):
            mn=ss[i]
            mnp=i
    if(mnp<mxp):
        time=mxp+(len(ss)-mnp-2)
    else:
        time=mxp+(len(ss)-mnp-1)
    return time

ans=arrival(input())
print(ans)