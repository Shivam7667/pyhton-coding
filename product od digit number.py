num = int(input('enter the number : '))
product = 1
while(num > 0):
    rem = num%10
    num = num//10
    product = product * rem
print('product of digit of a number is  : ',product)
