def analyze_text(s1):
  s1 = s1.replace(".", "")
  s1 = s1.replace(",", "")
  s1 = s1.lower()
  words_list = s1.split(" ")

  print (len(words_list), words_list)

  unique_words = list(set(words_list))
  print (len(unique_words), unique_words)

  word_frequency = {}

  for word in unique_words:
    word_frequency[word] = words_list.count(word)
  
  print(word_frequency)

  # sort based on frequency
  sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
  print(sorted_word_frequency)

  # Print top 3 words
  top_3_words = list(sorted_word_frequency.keys())[:3]
  print(top_3_words)

s1="Python is amazing. Python makes data analysis easy.Data analysis with Python is powerful and easy."
analyze_text(s1)