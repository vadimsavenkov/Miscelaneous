
def main(x)
  data = open('task_list.txt').read()
  word_count = data.capitize()
  
  print("Occurrences of the word:")
  print(word_count)
  return word_count
  
  
main("capital")