def validMove(grid,visited,i,j):
    return 0<=i< len(grid) and 0<=j<len(grid[0]) and grid[i][j]!='#' and not visited[i][j]

def dfs(grid, visited, i, j):
    if not validMove(grid,visited,i,j):
        return 0
    visited[i][j] = True
    diamonds=0
    if grid[i][j]=='D':
        diamonds=1
    moves=[(0,1),(0,-1),(1,0),(-1,0)]
    for move in moves:
        ni,nj =i+move[0],j+move[1]
        diamonds+=dfs(grid,visited,ni,nj)
    return diamonds

def mdiamonds(grid):
    mxdiamonds=0
    r,c=len(grid),len(grid[0])
    print(c)
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='.':
                visited=[[False]*c for _ in range(r)]
                mxdiamonds=max(mxdiamonds,dfs(grid,visited,i,j))
    return mxdiamonds

c=1
while c<8:
    input=open(f'input6_{c}.txt', 'r')
    nm=input.readline()
    nms=nm.split(' ')
    n,m=int(nms[0]),int(nms[1])

    grid=[]
    for i in range(n):
        s=input.readline()
        grid.append(s)

    res=mdiamonds(grid)
    # print(res,end='\n')

    output=open(f'output6_{c}.txt', 'w')
    output.write(f'{res}')
    output.close()
    c+=1