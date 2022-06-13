file=open("dataset/romeo.txt")
x=file.read()
d=x.split()
lis=list()
for i in d:
  if i in lis:
    continue
  else:
    lis.append(i)
    
lis.sort()
for i in lis:
  print(i)
file.close()