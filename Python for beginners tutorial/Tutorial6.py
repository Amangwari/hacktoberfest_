#Dictonary & and its functions

# Dictonary is nothing but key value pairs...It is case sensitive

d1 = {}
print(type(d1))

d2 = {"Aman":"Burger",
      "Harry":"fish", "Sheetal":"Roti",
      "Abhishek":{"Breakfast":"Roti",
                  "Lunch":"Pizza",
                  "Dinner":"Chicken"}}

d2["Ankit"] = "Junk Food"
d2["Rohit"] = "Momos"

print(d2["Aman"])
print(d2["Abhishek"])      #Will show the dictionary key
print(d2["Abhishek"]["Lunch"])     #dictionary in dictionary
print(d2)

del(d2)["Rohit"]              #Will delete shalimar from the dictionary
print(d2)


#Functions in dictionary
# d3 = d2        #here d3 is a pointer which is pointing on dictionary... and d2 is pointion itself...you will thing d3 will create a new
# del d3["Aman"]  #dictionary but here d3 is refrencing d2... if we remove something from d3 then automatically d2 element will also remove
# print(d2)      #so we use copy function

d3 = d2.copy()
del d3["Aman"]
print(d2)
print(d3)     #here you can see that element from d3 is deleted without deleting d2 element


#To get value
print(d2.get("Harry"))
d2.update({"Sohan":"Toffee"})      #To update
print(d2)

print(d2.keys())
print(d2.items())