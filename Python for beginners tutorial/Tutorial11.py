#For loops in python


list1 = [["Aman", 1], ["Shubham", 3], ["Rohit", 6], ["Vikram", 10]]        #This is list of list

tp = ("Aman", "Shubham", "Rohit", "Vikram")    #tuple

# print(list1[0], list1[1], list1[2])


print("\n")

#Using list
for item, lollypop in list1:
    print(item, "eats", lollypop ,"lollypops")

print("\n")

#Using tuple
for item in tp:
    print(item)

print("\n")

#To typecast into dictionary
dict1 = dict(list1)
# print(dict1)
for item, lollypop in dict1.items():
    print(item, "eats", lollypop, "lollypops")

print("\n")