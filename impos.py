s = input()
a = input()
b = input()

n = 0
l = [s]

def f(s, s1, s2):
  ns = s.replace(s1, s2)
  return ns

while n <= 1000:
  if a == b and a in s:
    print('Imposiburu')
    break
  v = f(l[-1], a, b)
  n += 1
  l.append(v)
  if l[-1] == l[-2]:
    print(len(l)-2)
    break
else: print('Imposiburu')

