# *args and **kwargs in python

'''def function_name_print(a, b, c, d):
    print(a, b, c, d)

function_name_print("Aman", "Harry", "Abhishek", "Rohit")'''

def funargs(Anita, *args, **kwargs):
    # print(type(args))
    # print(args[0])

    print(Anita)
    for item in args:
        print(item)

    print("\n")

    print("**Now i would like to introduce some of our heroes**")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

har = ["Harry", "Rohan", "Aman", "Shivam", "Rohit", "The Programmer"]
Anita = "I am a normal argument and the student are:"

kw = {"Harry":"Monitor","Rohan":"Student", "Aman":"Instructor", "Rohit":"Coordinator",
      "The programmer":"Python senior programmer", "Shivam":"Cook"}
funargs(Anita, *har, **kw)