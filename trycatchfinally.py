try:
    with open("test2.txt",'r') as reader:
        reader.read()
except Exception as e:
    print(e)
Finally:\
    print("Cleanup all records")