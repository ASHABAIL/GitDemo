i=4

while i>1:
    print(i)
    i = i-1
print("While loop execution is completed")

#while continue

it = 10

while it>1:
    if it==9:
        it = it -1
        continue
    if it==3:
        break
        print(it)
    it = it-1