# Tuples

f=open("dataset/mbox-short.txt","rt")
di={}
for i in f:
    if i.startswith("From") and not i.startswith("From:"):
        x=i.split()
        y=str(x[5])
        h=y[0:2]
        if h in di:
            di[h]=di[h]+1;
        else:
            di[h]=1
for i in sorted (di.keys()):
     print(i, di[i])