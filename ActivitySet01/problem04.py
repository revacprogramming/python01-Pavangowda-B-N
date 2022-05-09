# Conditional Execution

h=float(input("Enter Hour:"));
r=float(input("Enter Rate:"));
pay=h*r;
if h>40:
    res=pay+((h-40)*(r*0.5));
else:
    res=pay;
print(res);
#1.5
#done