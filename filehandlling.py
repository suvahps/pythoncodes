with open("file1.txt","a")as data:
    data.write("god is good")              #file handling used to create and adding data to a file





a=["abi","manu","sunil"]
for i in a:
    with open("file.txt","a")as  data:
        data.write("name: "+i+"\n")
    
