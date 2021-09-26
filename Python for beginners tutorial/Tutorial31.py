#Anonymous/ Lambda Functions in python : it is one liner function

# def minus(x, y):
#     return x - y

        # OR

minus = lambda x,y:  x-y

        # are same

print(minus(9, 4))


print("\n")
print("\n")



#now we use sort function with lambda
'''def a_first(a):
    return a[1]

a = [[1,14], [5,6], [8,23]]
a.sort(key=a_first)
print(a)'''


# insted of doing this we can also write this as
a = [[1,14], [5,6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)
