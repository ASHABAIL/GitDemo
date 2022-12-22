#Lists
list1 = [1, "great",9,4.8,"a",7,10]
print(list1)

print(list1[1])
print(list1[3])
list1 = [1, "great",9,4.8,"a",7,10]
print(list1)

print(list1[1])
print(list1[-2])
print(list1[1])
#insert the value
print(list1[1:3])# ['great',9]
list1.insert(2,"hello")
print(list1)
#append the value
list1.append(1)
print(list1)

#update the value
list1[1] = "GREAT"
print(list1)

#delete value

del list1[3]
print(list1)

