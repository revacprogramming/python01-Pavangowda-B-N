fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    x=line.split()
    for i in x:
       if not i in lst:
       		lst.append(i) 

lst.sort()
print(lst)
 