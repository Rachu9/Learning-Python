#List 
''' List is a collection of Items.
[]
oredered
mutable
allows duplicate values
It can contain differrent data type
'''

a=[1,2,3,4,5]
print(a)

a=[1,2,3,4,5,"hello"]
print(a)
print(type(a))
print(a[0])
print(a[-1])
a.pop()
print(a)
a.append("Hii")
print(a)
a.remove("Hii")
print(a)
a.insert(3,3)
a[2]=100
print(a)


print(len(a))

print(sorted(a))

print(a.index(2))

print(a.count(3))


 

print(a.sort())



print(a[:3])
print(a[::2])
print(a.clear())

