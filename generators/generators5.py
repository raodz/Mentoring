txt = 'The quick brown fox jumps over the lazy dog is an English-language pangram—a ' \
      'sentence that contains all of the letters of the English alphabet'
length_of_words = [len(word) for word in txt.split(' ') if word not in ['the', 'The']]
print(length_of_words)
