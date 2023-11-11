def dp(t):
    for i in range(0,t):
        s=input()
        s1=s.split(" ")
        a=int(s1[0])
        b=int(s1[1])
        if(a%b==0):
            print(0)
        else:
            m=a//b
            n=(m+1)*b
            print(n-a)
        

dp(int(input()))