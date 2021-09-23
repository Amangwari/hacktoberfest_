#Operators in Python
'''
Arithmatic Operator
Assignment Operator
Comparision Operator
Logical Operator
Identity Operator
Membership Operator
Bitwise Operator
'''

print("ARITHMATIC OPERATORS")
print("100 + 2 is ", 100 + 2)
print("100 - 2 is ", 100 - 2)
print("100 * 2 is ", 100 * 2)
print("100 ** 2 is ", 100 ** 2)   #Exponential operator
print("15 % 6 is ", 15 % 6)       #Modulus opereator gives us a remiander of the division
print("100 / 2 is ", 100 / 2)
print("15 // 6 is ", 15 // 6)    #Floor division method....gives us result before point

print("\n")

print("ASSIGNMENT OPERATORS")    #To assign a value on a numberor variable
x = 5
print(x)

x += 7      #increament of 7 in x
print(x)

x /= 3
print(x)

x *= 3
print(x)

x -= 3
print(x)

x %= 4
print(x)

print("\n")

print("COMPRARISON OPERATOR")
i = 8
print(i == 5)    #returns false coz 8 is not equal to 5
print(i != 5)
print(i >= 5)
print(i <= 5)

print("\n")

print("LOGICAL OPERATOR")
a = True
b = False

print( a and b)
print( a or b)

print("\n")

print("IDENTITY OPERATOR")
m = 5
n = 8
print( m is n)
print(m is not n)

print("\n")

print("MEMBERSHIP OPERATOR")
list = [3,3,4,2,23,44,556,34]
print(556 in list)
print(346 in list)
print(346 not in list)
print(3 in list)

print("\n")

print("BITWISE OPERATOR")
'''
0 - 00
1 = 01
1 - 10
3 - 11
'''

print(0 & 2)
print(0 | 3)
print("\n")

print(16%15//16)
print(1//16)

print("5 // 2 is ", 5 // 2)