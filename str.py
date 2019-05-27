with open('text.txt') as inf:
  s = inf.readline().strip()

n = len(s)-1
ns = ''
for i in range(n, -1, -1):
  #print('i =', i, 's[i] =', s[i])
  if s[i].isdigit() == True and s[i-1].isdigit() == True:
    digit = int(s[i-1] + s[i]) - int(s[i-1] + s[i])// 10
    ns += s[i-2] * digit
    i -= 2
  elif s[i].isdigit() == True and s[i-1].isdigit() == False:
    digit = int(s[i])
    ns += s[i-1] * digit
    i -= -1

result = ''
ouf = open('result.txt', 'w')
for i in range(len(ns)-1, -1, -1):
  result += ns[i]
ouf.write(result + '\n')
ouf.close
print(result)
