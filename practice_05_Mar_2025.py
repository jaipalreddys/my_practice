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

# tuples are immutable and are created using parentheses.
"""
Tuples are one of the built-in data structures in Python. Just like lists, tuples can hold a sequence of items and have a few key advantages:

Tuples are more memory efficient than lists
Tuples have a slightly higher time efficiency than lists
This is mostly because tuples are immutable, meaning we can’t modify a tuple’s elements after creating one, and do not require an extra memory block like lists. Because of this, tuples are great to work with if you are working with data that won’t need to be changed in your code.

In this article, we’ll cover features of tuples, indexing, and common built-in methods and functions that can be used with tuples.

Tuples
In Python, tuples are defined with parentheses () with comma-separated values. Just like lists, tuples are sequences and can hold objects of different data types.

This tuple has 4 items. We can see that we have 4 items separated by commas:

my_tuple = ('abc', 123, 'def', 456)

Tuples are capable of holding one item as long as the item is followed by a comma:

my_tuple = ('abc',)

Tuple Indexing and Slicing
Items in a tuple can be accessed with their index, otherwise known as their position in the tuple. Take a look at the following tuple:

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

Indices can be used to access specific items of this tuple. For example, if we want to access the first item, we can use index 0 (remember that Python is a zero-index language!). We write the name of the tuple followed by brackets [] that contains the index to access the item. This code would print the first item, ’abc’.

print(my_tuple[0]) # prints abc

We can also apply slicing, using a range of indices to access multiple items just like in a list. The brackets should contain the first index as well as the index of the end of the item, separated by :. This code would print the items at positions 3 and 4:

print(my_tuple[3:5]) # prints (456, 789)

Common Built-in Functions
In contrast to lists, tuples have a limited number of built-in functions as they are immutable. We’ll take a look at a few built-in functions below:

len()
The length of a tuple can be measured using the built-in function len(). It takes the tuple as an argument to count the items in the tuple.

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(my_tuple)) # prints 6

max()
The built-in function max() returns the tuple’s maximum value. Note that this function requires all of the values to be of the same data type. If used with numerical values, the function returns the maximum value. If used with string values, the function returns the value at the tuple’s maximum index as if it was sorted alphabetically. The string closer to the letter “Z” in the alphabet would have a higher index.

my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
 
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"
 
my_tuple = ('abc', 234, 567, 'def')
max(my_tuple) # throws an error!

min()
The built-in function min() returns the tuple’s minimum value. Similar to the max() function, the min() function requires all of the values to be of the same data type. If used with numerical values, the function returns the minimum value. If used with string values, the function returns the value at the tuple’s minimum index as if it was sorted alphabetically. The string closer to the letter “A” in the alphabet would have a lower index.

my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"
my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!

.index()
The built-in method `.index()’ takes in a value as the argument to find its index in the tuple.

my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

.count()
The built-in method `.count()’ takes in a value as the argument to find the number of occurrences in the tuple.

my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1

"""

# zip() function is used to combine two lists into a list of tuples.

"""
In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. 
One of those functions is zip().

The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists. 
While zip() can work with many different scenarios, we are going to explore only a single one in this article.

Let’s use a list of student names and associated heights as our example data set:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
Suppose that we already had a list of names and a list of heights:

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

If we wanted to create a nested list that paired each name with a height, we could use the built-in function zip().

The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs. 
Each pair contains one element from each of the inputs. This is how we would do it for our names and heights lists:

names_and_heights = zip(names, heights)

If we were to then examine this new variable names_and_heights, we would find it looks a bit strange:

print(names_and_heights)

Would output:

<zip object at 0x7f1631e86b48>

This zip object contains the location of this variable in our computer’s memory. 
Don’t worry though, it is fairly simple to convert this object into a useable list by using the built-in function list():

converted_list = list(names_and_heights)
print(converted_list)

Outputs:

[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]

Notice two things:

Our data set has been converted from a zip memory object to an actual list (denoted by [ ])

Our inner lists don’t use square brackets [ ] around the values. 
This is because they have been converted into tuples (an immutable type of list).  
"""

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
