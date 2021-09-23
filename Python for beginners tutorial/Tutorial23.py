#Seek(), tell() & More on Python files

f = open("Aman4.txt")
print(f.tell())            #to know where is file pointer (character)
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()

f = open("Aman5.txt")
print(f.readline())
f.seek(0)
print(f.readline())
f.seek(10)               #resets the file pointer and goes where we give input and Reads after 5th character
print(f.readline())

f.close()
