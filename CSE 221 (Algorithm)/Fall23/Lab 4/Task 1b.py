def adjacencyList(res,ui,vi,wi):
    if len(res)<ui+1:
        res.extend([]for _ in range(ui+1-len(res)))
    res[ui].append((vi,wi))
    return res

c=1
while c<4:
    input=open(f'input1b_{c}.txt','r')
    nm=input.readline()
    nms=nm.split(' ')
    m,res=int(nms[1]),[]

    for i in range(m):
        s=input.readline()
        ss=s.split(' ')
        res=adjacencyList(res,int(ss[0]),int(ss[1]),int(ss[2]))
    input.close()

    output=open(f'output1b_{c}.txt','w')
    for i in range(len(res)):
        output.write(f'{i} : {res[i]}  \n')
        print(f'{i} : {res[i]}  \n')
    output.close()
    print('\n')
    c+=1
