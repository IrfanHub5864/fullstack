with open("file.txt","r") as file:
    content=file.read()
word=content.split()
print("the word count is", len(word))
