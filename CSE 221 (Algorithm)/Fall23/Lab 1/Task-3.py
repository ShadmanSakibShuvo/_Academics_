def sort(id,mark):
    for i in range(len(mark)):
        maxmark=0
        maxmarki=0
        for j in range(i,len(mark)):
            if mark[j]>maxmark or (mark[j]==maxmark and id[j]<id[maxmarki]):
                maxmark=mark[j]
                maxmarki=j
        mark[i],mark[maxmarki]=mark[maxmarki],mark[i]
        id[i],id[maxmarki]=id[maxmarki],id[i]
    return id,mark

input=open('/content/drive/MyDrive/221 lab input files/Lab 1/input3.txt','r')
N=int(input.readline())
id,mark=[],[]
s1=input.readline()
ss1=s1.split(' ')
s2=input.readline()
ss2=s2.split(' ')
for i in range(N):
  id.append(int(ss1[i]))
  mark.append(int(ss2[i]))

sort(id,mark)

output=open('/content/drive/MyDrive/221 lab input files/Lab 1/output3.txt','w')
for i in range(N):
  output.write(f'ID: {id[i]} Mark: {mark[i]}')
  if i!=N-1:
    output.write('\n')
output.close()