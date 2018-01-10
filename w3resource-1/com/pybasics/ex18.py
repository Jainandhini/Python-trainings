#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

a=input("enter no1: ");
b=input("enter no2: ");
c=input("enter no3: ");
sum=a+b+c;
if(a==b==c):
    print(sum**3)
else:
    print sum