def computepay(h, r):
    if h<=40:
        res=h*r;
    elif h>40:
        res=(h*r+((h-40)*(r/2)))
    return res

hrs = float(input("Enter Hours:"))
rate=float(input("Enter Rate:"))

p = computepay(hrs,rate)
print("Pay", p)