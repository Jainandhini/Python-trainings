#Write a Python program to test whether a number is within 100 of 1000 or 2000.

n=input("Enter a number: ");
a1=abs(1000-n);
a2=abs(2000-n);
if a1<=100 or a2<=100:
    print("Number is within 100 of 1000 or 2000");
else:
    print("Out of range");