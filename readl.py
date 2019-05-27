d = {i: [0,0] for i in range(1, 12)}
with open('dataset_3380_5 .txt') as inf:
  for line in inf:
    cl, name, height = line.split('\t')
    cl = int(cl)
    d[cl][0] += int(height)
    d[cl][1] += 1
for key in range(1, 12):
  if d[key][1] != 0:
    d[key] = float(d[key][0] / d[key][1])
    print(key, d[key])
  else:
    d[key] = '-'
    print(key, d[key])
