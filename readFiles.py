
menufile = open('test1.txt')
print(menufile.read(8))

print(menufile.readline())
print(menufile.readline())
menufile.close()


line = menufile.readline()
while line!= "":
    print(line)
    line = menufile.readline()

menufile.close()


f=open('test1.txt')
print(f.read())
f.readline()
f.readline()
l1 = f.readline()
while l1!= "":
    print(l1)
    l1 = f.readline()
f.close()

f = open('test1.txt')
for line in f.readlines():
    print(line)
f.close()

