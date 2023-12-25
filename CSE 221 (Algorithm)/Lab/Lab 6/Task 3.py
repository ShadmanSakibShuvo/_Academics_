class DisjointSet:
    def __init__(self,n):
        self.p=[i for i in range(n+1)]
        self.r=[1]*(n+1)

    def find(self,u):
        if self.p[u]==u:
            return u
        self.p[u]=self.find(self.p[u])
        return self.p[u]

    def union(self,u,v):
        ru=self.find(u)
        rv=self.find(v)

        if ru!=rv:
            if self.r[ru]>self.r[rv]:
                ru,rv=rv,ru
            self.p[ru]=rv
            self.r[rv]+=self.r[ru]

def main():
    input=open(f'input3.txt','r')
    inp=input.readline()
    N,K=map(int,inp.split(' '))
    ds=DisjointSet(N)

    output=open('output3.txt','w')
    for _ in range(K):
        inp=input.readline()
        A,B=map(int, inp.split(' '))
        ds.union(A,B)
        print(ds.r[ds.find(A)])
        output.write(f'{ds.r[ds.find(A)]}\n')
    output.close()

if __name__ == "__main__":
    main()
