# These "Difficult Python Code Challenges Involving Dictionaries" are actually from the Learn Python 3 course that I completed in Codecademy in December.

# WORD LENGTH DICTIONARY

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  return {word:len(word) for word in words}

# compare solution above to solution without dictionary comprehension that follows
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# More guidance on dict comprehensions: https://www.datacamp.com/community/tutorials/python-dictionary-comprehension


# FREQUENCY COUNT

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
# The function should return a dictionary containing the frequency of each element in words.

# Write your frequency_dictionary function here:
#from collections import Counter

def frequency_dictionary(words):
  frequency = {}
  for word in words:
    if word not in frequency:
      frequency[word] = 0
    frequency[word] += 1
  return frequency

#Alternatively you can use this much shorter solution, which utilises Counter.

def frequency_dictionary(words):
  return dict(Counter(words))

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# UNIQUE VALUES

# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.

# Write your unique_values function here:
# Write your unique_values function here:
def unique_values(my_dictionary):
  return len(set(my_dictionary.values()))

#Alternatively this longer solution is how you could do it without using sets.
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#COUNT FIRST LETTER

# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

# So in example above, the function would return:
# {"S" : 4, "L": 3}

# Write your count_first_letter function here:
from collections import defaultdict

def count_first_letter(names):
  d = defaultdict(int)
  for name in names:
    first_letter = name[0]
    d[first_letter] += len(names
    [name])
  return dict(d)

#Alternatively, the following solution is without defaultdict.

def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
{"S" : 4, "L": 3}
