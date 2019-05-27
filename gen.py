with open('result.txt') as inf:
  genome = inf.readline().strip()
print(genome)
s = 1
i=0
gnm=''
n=len(genome)-1
if n==0:
  gnm=gnm+genome[n]+'1'
if genome[n-1]==genome[n]:
  while i<n:
    if genome[i]==genome[i+1]:
      s+=1   
      if i==n-1:
        gnm=gnm+genome[i]+str(s)
      i+=1
    else:
      gnm=gnm+genome[i]+str(s)
      i+=1
      s=1
 # print(gnm)
else:
  while i<n:
    if genome[i]==genome[i+1]:
      s+=1
      i+=1
    else:
      gnm=gnm+genome[i]+str(s)
      i+=1
      s=1
  gnm=gnm+genome[n]+'1'
print(gnm)

ouf = open('rev.txt', 'w')
ouf.write(gnm)
ouf.close

