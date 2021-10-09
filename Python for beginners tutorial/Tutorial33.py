# F-Strings & String Formatting in python - TO insert/format a variable in a string
import math

me = "Aman"
a1 = 3

# a = "this is %s"%me     #these are also a methods to format string but it is to messy with many variables
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)

a = f"This is {me} {a1} {20 * 3} {math.cos(90)}"
print(a)