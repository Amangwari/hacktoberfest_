#Using with Block to open python files

with open("Aman5.txt") as f:
    # a = f.readline(4)
    a = f.readlines()
    print(a)

f = open("Aman5.txt")
print(f.readlines())
# print(f.readline())

