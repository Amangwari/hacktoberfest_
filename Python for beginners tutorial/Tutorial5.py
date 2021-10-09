# List and List functions in python

grocery = ["Soap","Vimbar","Perfume",
         "Fortune oil", 56]

print(grocery)
print(grocery[3])

numbers = [2,4,9,11,3]
print(numbers)
print(numbers[3])

#List methods
numbers.sort()    #To sort numberts in increasing order
print(numbers)

numbers.reverse()     #To reverse numbers from backwards
print(numbers)

#Slicing
print(numbers[:])
print(numbers[1:4])

#Extended slice
print(numbers[::2])
print(numbers[::3])

print(numbers[::-1])


#List methods
numbers.insert(1,44)      #inserts element b/w the list. 1= index number, 44 = what number you want to add
print(numbers)

numbers.remove(2)        #Removes particular element from the list
print(numbers)

numbers.pop()             #Removes last element of the list
print(numbers)

numbers = []
numbers.append(7)
numbers.append(12)
numbers.append(71)
print(numbers)


numbers[1] = 98   #To change value in index
print(numbers)


#mutabel :- can change
#immutable :- cannot change

tp = (1, 2, 3)    #The element of the touple cant be changed
print(tp)

tp = (1,)  #if we want only one element in tuple so we have to put a comma after the element
print(tp)

# tp[1] = 8   #will not change the value of a touple because it is immutable
# print(tp)


#HOW TO SWAP TWO NUMBERS

#traditional way
a = 1
b = 8
temp = a
a = c
b = temp
print(a,b)

#Using python
a = 2
b = 4
a, b = b, a
print(a,b)

