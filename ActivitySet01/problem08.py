# Use the file name mbox-short.txt as the file name
add=0;
counter=0;
fname = input("Enter file name: ")
fh = open(fname,"rt")
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue;
    elif  line.startswith("X-DSPAM-Confidence:"):
        ind=line.find("0.");
        num=(line[ind:]);
        float_num=float(num)
        add+=float_num;
        counter+=1;
avg=add/counter;
print(f"Average spam confidence: {avg}");
