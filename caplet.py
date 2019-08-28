def main():
     f = open("tasks_list.txt").read()
     capital_letters = f.title()
     #print(capital_letters)
     
     
     words=capital_letters.split()
     #words is a [] after you use the split function which contains 
     #the words of the sentence splitted by space blanks between them
     #print(words)
     
     
     for word in words:
         print(word)
         #print("\n")
     #print(capital_letters)
    
     
main()

def main():
    with open("tasks_list.txt", "r") as f:
     
     for line in f:
        capital_letters = line.title() 
        print(capital_letters)
       
main()
