class kruskal: 
    def __init__(self,v): 
        self.V = v 
        self.G=[] 

    def addEdge(self,u,v,w): 
        self.G.append([u,v,w]) 

    def find(self,p,i): 
        if p[i]!=i: 
            p[i]=self.find(p,p[i]) 
        return p[i] 

    def union(self,p,r,x,y): 
        if r[x]<r[y]: 
            p[x]=y 
        elif r[x]>r[y]: 
            p[y]=x 
        else: 
            p[y]=x 
            r[x]+=1

    def MST(self): 
        res=[] 
        i=0
        e=0
        self.G=sorted(self.G,key=lambda item: item[2]) 
        p=[] 
        r=[] 
        for n in range(self.V+1): 
            p.append(n) 
            r.append(0) 

        while e<self.V-1: 
            u,v,w=self.G[i] 
            i=i+1
            x=self.find(p,u) 
            y=self.find(p,v) 
            if x!=y: 
                e=e+1
                res.append([u,v,w]) 
                self.union(p,r,x,y) 
  
        cost=0
        for u,v,w in res: 
            cost+=w
        return cost 

if __name__ == '__main__':
    input=open(f'input4.txt','r')
    inp=input.readline()
    N,M=map(int,inp.split(' ')) 
    g=kruskal(N)
    for _ in range(M):
        inp=input.readline()
        u,v,w=map(int,inp.split(' ')) 
        g.addEdge(u,v,w) 
    print(g.MST())
    output=open('output4.txt','w')
    output.write(f'{g.MST()}')
    output.close() 