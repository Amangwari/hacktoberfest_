#Exercise 1
#Create a dictionary and take input from the user and return the meaning og the word from the dictionary

print("***WELCOME TO THE MINI PYTHON DICTIONARY***")
d1 = {"Master":"गुरुजी", "Buisness":"व्यापार", "Yourself":"स्वयं", "Intrested":"इच्छुक"}

Search = input("Enter your word:- ")
b = Search.capitalize()
print(b," = ",d1 [b])
print("***THANKS FOR USING MINI PYTHON DICTIONARY")