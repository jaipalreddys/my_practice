# inbuilt functions: insert()
# insert() method is used to insert an element at a given index in the list.
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line) 


front_display_list.insert(0,'Pineapple')
print(front_display_list)

# pop() method is used to remove an element from the list.

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)
removed_element_two = cs_topics.pop(2)
print(cs_topics)
print(removed_element_two)

removed_chapter = data_science_topics.pop()
print(data_science_topics)
print(removed_chapter)

remove_algorithms = data_science_topics.pop(3)
print(data_science_topics)
print(remove_algorithms)

# range() function is used to generate a sequence of numbers.

# Your code below: 

number_list = range(3)
print(list(number_list))

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_range = range(10)
print(list(my_range))

number_list = range(9)
print(list(number_list))

zero_to_seven =range(8)
print(list(zero_to_seven))

# Your code below: 

range_five_three = range(5, 15, 3)

my_list = range(2,9)
print(list(my_list))

my_range = range(2,9,3)
print(list(my_range))

my_range3 = range(1,100,10)
print(list(my_range3))

range_diff_five = range(0,40,5)
print(range_diff_five)

# len() function is used to get the length of the list.

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below: 

my_list = [1,2,3,4,5]
print(len(my_list))

long_list_len = len(long_list)
print(long_list_len)

list_new = list(big_range)
big_range_length = len(list_new)
print(big_range_length)
print(len(big_range))

big_range = range(2,3000,100)
big_range_length = len(big_range)
print(big_range_length)

# slicing lists

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]

# Your code below: 

letters =["a","b","c","d","e","f","g"]

letters_new = letters[1:6]
print(letters_new)

print(beginning)

beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

fruits =["apple","cherry","pineapple","orange","mango"]

sdf = fruits[-2:]
print(sdf)

print(fruits[-1:])

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three )

#counting elements in a list

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("s")
print(num_i)

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

num_pairs = number_collection.count([100,200])
print(num_pairs)

jake_votes = votes.count("Jake")
print(jake_votes)

# sorting lists

names =["Xander", "Buffy", "Angel","Willow","Giles"]
names.sort()
print(names)
sdf = names.sort(reverse = True)
print(sdf) # will return none

""" Note: The .sort() method does not return  any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable. """


# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses)


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()
print(sorted_cities)
print(cities)

cities.sort(reverse=True)
print(cities)

# sorted() function is used to sort the list without modifying the original list.

names =["Xander","Buffy","Angel","Willow","Giles"]
sorted_names = sorted(names)
print(sorted_names)
print(names)

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:

games_sorted =  sorted(games)
print(games_sorted)
print(games)


# Review

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)
 
first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[:3]
print(first_3)

twin_beds = inventory.count("twin bed")
print(twin_beds)

removed_item = inventory.pop(4)
print(removed_item)

inventory.insert(10,"19th Century Bed Frame")

print(inventory)

inventory.sort()
print(inventory)

inventory.sort(reverse=True)
print(inventory)

new_inventory = sorted(inventory)
print(new_inventory)


