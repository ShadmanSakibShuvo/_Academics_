s=input()
s1=s.split(' ')
ss=[]
ss.append(int(s1[0]))
ss.append(int(s1[1]))
if(ss[0]%2==0):
    if((ss[0]//2)>=ss[1]):
        print((2*ss[1])+1)
    else:
        print(2*ss[1])