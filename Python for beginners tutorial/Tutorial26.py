#Scope, Global Variables and Global Keyword

l = 10  #Global variable
def function1(n):
    l = 5   #Local variable
    m = 6   #local variable
    l = l + 2     #Adds  +2 on local variable l
    print(l, m)

    #To change value of global variable inside local variable scope
 #    global l
 #    l = l + 20
 #    print(l)
    print(n, "I have Printed")

function1("This is me")
l = l + 2    #To change value of global variable outside the local variable scope
print(l)

print("\n")
print("\n")

x = 88
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)