#QUIZ : make a list in which number and characters or anything but print the numbers which are greater than equal to 6

items = ["Aman" ,int ,float ,2, "Tushar",34 ,56 ,334 ,"Raja", "Abhishek", "Mohit", 43 ,23 ,"l",99, 6 ,8 ,"Sahil"]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)