def main(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].lower() + " "
     return result[:-1]  
     
print(main("go to grocery feed dog do homework go to gym"))




