# Dictionaries

f=open("dataset/mbox-short.txt","rt")

di=dict()
largest=0
lookvalue=None
for i in f:
    if i.startswith("From") and not i.startswith("From:"):
        x=i.split()
        fin=x[1]#find the email value
        
        if fin in di:
            di[fin]=di[fin]+1
        else:
            di[fin]=1
        #print(x[1])
for k in di:
    if largest<di[k]:
        largest=di[k]
        lookvalue=k;
print(lookvalue,largest)