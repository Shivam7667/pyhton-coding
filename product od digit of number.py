# Write a Python program to calculate product of digits of a number.
n = int(input("enter the number :"))
product = 1
while(n>0):
    rem = n%10
    n = n//10
    product = rem * product
print("product of number of digit :",product) 
