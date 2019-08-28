def main(word):
  data = open('repeated_words.txt').read()
  word_count = data.count(word)
  
  print("Occurrences of the word:")
  print(word_count)
  return word_count
  
  
main("star")

