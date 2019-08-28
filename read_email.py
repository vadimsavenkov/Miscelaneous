
fileData=open("email.txt")
lines=fileData.readlines()
ignore=["a", "for", "in","and", "as", "is", "the", "b"]
for line in lines:
    words=line.split()
    for word in words:
        if word not in ignore:
            print(word)
        #print(word)