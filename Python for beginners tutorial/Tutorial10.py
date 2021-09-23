# Exercise-2 Faulty Calculater
# Design a  calcualter which will perform corectly all the problems except following ones:
# 45*3=555, 56+8=77, 56/6=4

# Your program should take operator and the two numbers as input form and then retun the result

print("Please enter your 1st number")
num1 = int(input())

print("Please enter your 2st number")
num2 = int(input())

print("Enter your operator")
O = input()

if O == "*":
    if num1*num2 == 45*3:
        print("555")
    else:
        print(num1 * num2)

elif O == "+":
    if num1+num2 == 56+9:
        print("77")
    else:
        print(num1+num2)

elif O == "/":
    if num1/num2 == 56/6:
        print("4")
    else:
        print(num1/num2)

else:
    print(num1-num2)

print("Thanks for using calculator")