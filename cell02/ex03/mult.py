#!/usr/bin/env python3
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
result = num1 * num2
print (f"{num1} x {num2} = {result}")
if result >0 :
    print("the result is positive.")
elif result < 0 :
    print("The result is nigative.")
else :
    print("the result is both positive and nigative.")