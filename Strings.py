str1 = "Pavani.RAJ "
str2 = "Hemanth/raj"
str3 = "Pav"
print(str1 + str2)
if str3 in str1:
    print("pav is present in str1")
else:
    print("pav is not present in str1")

print (str2 in str1) #substring check

#split is used to spit the two words
value = str1.split(".")
print(value)
print(value[1])
print(str1[0:3]) #to get substrings in python


print(str2.split("/"))
#strip is used to remove the white spaces

str5 = " this is Great "
print(str5.rstrip())
print(str5.lstrip())