"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
"""
file=open("dataset/romeo.txt","r")
l=list()
for line in file:
    line=line.rstrip()
    line=line.split()
    for i in line:
        if not i in l:
            l.append(i)
        else:continue
l.sort()
print(l)