#Exercise 4 :- Astrologer's Stars

'''
Pattern printing

input = integer n
boolean = True or false

if True
*
**
***
****

if false
****
***
**
*
'''
print("***Pattern Printing***")
try:
    num = int(input("How many rows you want to print :- "))

except Exception as e:
    print("Invalid input...Please enter an integer")

print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False :- ")
if bool_val == "1":
    for i in range(0,num+1):
        print("*"*i)

elif bool_val == "0":
    for i in range(num,0,-1):
        print("*"*i)

else:
    print("Invalid entry")

