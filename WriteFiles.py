#read the file and store all the lines in list
#reverse the list
#write the list back to the file

#with open("test1.txt",'r') as file:
#    line1 = file.readlines()
 #   reversed(line1)
  #  with open('test1.txt','w') as file2:
   #     for line in reversed(line1):
    #        file2.write(line)

with open('test1.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test1.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)

with open ('text2.txt','r') as file1:
    value1 = file1.readlines()
    reversed(value1)
    with open ('text2.txt','w') as file2:
        for line in reversed(value1):
            file2.write(line)








