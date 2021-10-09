# Sets in python
s = set()
# print(type(s))

s_from_list = set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))

#To add elements in blank set
s.add(1)
# s.add(1)   #set retains unique value no.... repetation
s.add(2)
s.add(3)
s.add(4)
print(s)

#To remove element from set
s.remove(3)
print(r)


#Union
s1 = s.union({1,2,3,4,5})
print(s,s1)

#Intersection
s1 = s.intersection({1,2,3,4,5})
print(s,s1)

#Disjoint
s2 = {6,7}
print(s.isdisjoint(s1))

print(len(s))
print(min(s))
print(max(s))
