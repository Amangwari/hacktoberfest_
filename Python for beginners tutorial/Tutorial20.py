#Python File I/O Basics

'''
"r" :- Open file for reading
"w" :- open file for writing
"x" :- Creates files if not exist and if exists then operation will fail
"a" :- Add more content to a file(append)
"t" :- Text mode (for text files only)
"b" :- Binary mode (for binary files)
"t" :- Read and write file both
'''

#Open(), read() & Readline() for reading file

f = open("Aman.txt")
f = open("Aman.txt", "rt") #hence rt is a default mode.. no need to write it ..result will be constant we can also use "rb"
content = f.read()
print(content)

f.close()   #To close the file

print("\n")

f = open("Aman.txt")
content = f.read(4)
print(content)

content = f.read(3)
print(content)
f.close()

print("\n")

f = open("Aman.txt")
print(f.readlines())     #prints a list object
# print(f.readline())    #prints line wise line
# print(f.readline())
# print(f.readline())

print("\n")

f = open("Aman.txt")
# content = f.read()

for line in f:
    print(line, end="")

f.close()