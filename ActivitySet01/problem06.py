i=1;
while True:
    num=input("Enter number:");
    if num=="done":
        break;
    else:

            try:
                num=int(num)
                if i==1:
                    largest=num;
                    smallest=num;
                    i=0;
                if num>largest:
                    largest=num;
                elif num<smallest:
                    smallest=num;
            except:
                print("Invalid input")
                break
                
print("Maximum is ", largest)
print("Minimum is ", smallest)              