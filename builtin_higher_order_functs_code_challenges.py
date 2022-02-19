#MAP
#returned_map_object = map(function, iterable)

#Code Challenge

# Say we stored our course grades in a list, but some of the grades were on a four-point scale and others were on a 100-point scale. 
# To get all the grades on the same scale, try using a lambda function with the map() function to multiply just the grades on the four-point scale 
# by 25 to get all of the grades on the same 100-point-scale.

grade_list = [3.5, 3.7, 2.6, 95, 87]

# My code below:

grades_100scale = map(lambda input: input*25 if input<25 else input*1, grade_list)
updated_grade_list = list (grades_100scale)
print(updated_grade_list)


#FILTER

#Code Challenge
# We were given a list of lists, where each sublist holds the title of a famous book that has a year as its title and the last name of the author 
# that wrote the book. Unfortunately, when this list was made, each of the books was accidentally entered twice—once with the title as a numeric value 
# and once with the title as a string. Use the filter() function to deduplicate the list and keep only the sublists that have the book title stored as a string:

books = [["Burgess", 1985],
 ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
   ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
     ["Murakami", 1985]]

# My code below: 

string_titles = filter(lambda title: type(title[1]) == str, books) 
 
string_titles_list = list(string_titles)

print(string_titles_list)

# REDUCE

#Code Challenge
# Given a list of letters, use the reduce() higher-order function with a lambda function to combine the letters into a single word:

letters = ['r', 'e', 'd', 'u', 'c', 'e']

# My code below:

from functools import reduce
word = reduce(lambda x,y: str(x+y), letters)

print(word)


