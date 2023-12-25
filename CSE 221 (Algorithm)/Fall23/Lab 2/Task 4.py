def task2(arr,n):
    def sort2nd(arr):
        return arr[1]

    arr=sorted(arr, key=sort2nd)
    c=0
    k=0
    m=0

    while k<n:
        t2=[]
        if k>0:
            arr=t2
        for i in range(1,len(arr)):
            if arr[i][1]>=arr[m][1]:
                c+=1
                m=i
        k+=1

    return c

c = 1
while c < 3:
    with open(f'/content/drive/MyDrive/221 lab input files/Lab 2/input4_si{c}.txt','r') as input_file:
        n,m = map(int, input_file.readline().split())
        a1 = []

        for i in range(n):
            s = input_file.readline()
            ss = s.split(' ')
            a = []
            a.append(int(ss[0]))
            a.append(int(ss[1]))
            a1.append(a)

    m = task2(a1,n)

    with open(f'/content/drive/MyDrive/221 lab input files/Lab 2/output4_so{c}.txt','w') as output_file:
        output_file.write(f'{m}')

    c += 1