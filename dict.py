#Dictionary
'''
word-meaning
key-value
unordered
mutable
{}
'''

birthday={
    "Rachana":"09-05-2003",
    "Prajna":"09-09-2002",

}
print(birthday)
print(type(birthday))
print(birthday.keys())
print(birthday.values())

print(birthday.items())

print(birthday["Rachana"])

#safe access,It reduces program crash
print(birthday.get("Rachana"))
print(birthday.get("Rachu","Not Found"))

a=dict()
print(type(a))





#adding the new value to dictionary
birthday["Rachna"]="09-05-2003"
print(birthday)

#pop and del
birthday.pop("Rachna")
print(birthday)

# del birthday["Rachna"]

#clear -It clears the netire dictionary


a={"a":"Hii", "b":"Hello"}

b={"c":"Hii", "d":"Hello"}

a.update(b)
print(a)


i1={
    "name":"Tea",
    "amt":250
}


i2={
    "name":"sugar",
    "amt":250
}

print(i1["amt"]+i2["amt"])