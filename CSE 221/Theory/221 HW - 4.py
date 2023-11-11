def bs(a,n,T):
    l,r,c=0,n-1,0    #c is for finding error
    while l<=r:
        m=((l+r))//2
        if a[m]<T:
            l=m+1
        elif a[m]>T:
            r=m-1
        else:
            return m
        
            if c==0:   #checking if the algorithm is written wrong
                c=m
            if c!=m:
                raise RuntimeError
            
    return f'unsuccessful'

print(bs([23,2,19,3,7,11,5,13],8,2))