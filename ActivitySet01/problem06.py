#Loops and Iterations
"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""
i=1
while True:
    num1=input("Enter number : ");
    if num1=="done":
        break
    try:
        num1=int(num1)
        if i==1:
            largest=num1
            smallest=num1
            i=0
        if largest<num1:
            largest=num1
        elif smallest>num1:
            smallest=num1
    except:
        print("Invalid input")
        break
print(f"Maximum is {largest}");
print(f"Minimum is {smallest}");