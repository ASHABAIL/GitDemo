try:
    with open("test1.txt",'r') as Reader:
        Reader.read()
except:
    print("Test2.txt file path not found")

try:
    with open ("test2.txt",'r') as Reader:
        print("yes")
except Exception as e:
    print(e)
