# If Else & Elif Conditionals in Python

var1 = 6
var2 = 56

var3 = int(input())

if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")


list1 = [5,6,7,8]
if 5 in list1:
    print("Yes 5 is in the list")

if 13 not in list1:
    print("No it's not in the list")

print(15 not in list1)


"""Program taking age as a input from user:
                              if age>18 => you can drive
                                 age<18 => you cannot drive
                                 age==18 => you cannot drive
                                 age>10 and age<18:- Invalid entry"""

print("***Welcome to Indian driving school***")
print("Enter your age :-")
age = int(input())

if age>18 and age<100:
    print("You can drive")

elif age>10 and age<18:
    print("You are minor you cannot drive")

elif age == 18:
    print("Sorry we can't decide. so you should come here physically")

else:
    print("Invalid entry")


