def sort(names,times,others):
    for i in range(len(names)):
        minname='Z'
        minnamei=i
        for j in range(i,len(names)):
            if names[j]<minname or (names[j]==minname and times[j]>times[minnamei]):
                minname=names[j]
                minnamei=j
        names[i],names[minnamei]=names[minnamei],names[i]
        times[i],times[minnamei]=times[minnamei],times[i]
        others[i],others[minnamei]=others[minnamei],others[i]
    return names,times,others

names,times,others=[],[],[]

input= open('/content/drive/MyDrive/221 lab input files/Lab 1/input4.txt', 'r')
N=int(input.readline())

for i in range(N):
    s=input.readline().strip().split(' ')
    names.append(s[0])
    times.append(s[6])
    others.append(f'{s[1]} {s[2]} {s[3]} {s[4]} {s[5]}')

names,times,others=sort(names,times,others)

output=open('/content/drive/MyDrive/221 lab input files/Lab 1/output4.txt','w')
for i in range(N):
    output.write(f'{names[i]} {others[i]} {times[i]}')
    if i!=N-1:
      output.write('\n')
output.close()