with open("sample.txt","w") as file:
    file.write("This is my file\n")
with open("sample.txt","a") as file:
    file.write("Useless file")
with open("sample.txt","r") as file:
    content=file.read()
    print(content)