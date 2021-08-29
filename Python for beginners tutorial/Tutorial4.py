# String slicing and other function in python
mystr = "aman is a good boy"
mystr2 = "Aman Is a Good Boy"
print(mystr)

print(len(mystr))   #To check length of a string

print(mystr[3])      #To print 3rd character of the string
print(mystr[0:4])    #To print 0 to 4 characters of the strings
print(mystr[0:17])

#Character skips
print(mystr[0:18:2])    #in the last 2 shows the skipping ...it skips every 1 charcter from the string

#neagative indexes
print(mystr[-4:])
print(mystr[-4:-2])
print(mystr[15:17])

#To reverse a string
print(mystr[::-1])

#FUNCTIONS IN A STRING
print(type(mystr))
print(mystr.isalnum())           #Returning a boolean variable and returns false coz it is not alphanumeric

print(mystr.isalpha())           #Returning a boolean variable and returns false coz it is not aplha coz it has spaces

print(mystr.endswith("boy"))     #becuse the string is ending with boy
print(mystr.endswith("bboy"))    #becuse the string is not ending with bboy


print(mystr.count("o"))         #Counts the O in the string

print(mystr.capitalize())       #Capatalize the first character of the string

print(mystr.find("is"))         #finds the character in a string .... gives us a index value

print(mystr2.lower())          #converts whole string capital letters to small letters

print(mystr2.upper())          #Converts whole string small letters to capital letters

print(mystr2.replace("Is", "are"))      #To replace (is) character to (are) character in the string