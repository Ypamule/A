#Commenting is important for code readability and maintenance.
# There are two types of comments in Python: single-line comments and 
# multi-line comments.
# Single-line comments start with the hash character (#) and 
# extend to the end of the line.
# Multi-line comments can be created using triple quotes (''' or """).


#Variables in python
'''Variables are used to store data in Python. 
They are created when you assign a value to a name. 
Variables can be of different types, 
such as integers, floats, strings, and booleans. 
Variables are case-sensitive, 
so myVar and myvar are considered different variables.

There are rules for naming variables in Python. These includes:
1. Variable names must start with a letter 
or the underscore character.
2. Variable names cannot start with a number.
3. Variable names can only contain alpha-numeric characters 
and underscores (A-z, 0-9, and _ ).
4. Variable names are case-sensitive 
(age, Age and AGE are three different variables).
5. Variable names cannot be any of the Python keywords.'''


# variables assignment
# x = 5
# print(x)
# check the type of variable. we use the type() function to see the output of variable x, we use print() function.
# print(type(x))

# _firstname_ = "Kofi"
# print(_firstname_)
# print(type(_firstname_))


# ABC_123 = 3+2j
# print(ABC_123)
# print(type(ABC_123))


# healthy_fruits = ["Guava", "Mango", "Pineapple", "Grapes", "Tomatoes", "Avocado"]
# #print the list
# print(healthy_fruits)
# print(len(healthy_fruits))  # to check the length of the list
# print(type(healthy_fruits))  # to check the type of the list



#list in another list
# healty_vegetables = ["carrot","spinach","cabbage","onion","garlic"]
# healthy_food = [healthy_fruits, healty_vegetables]
# print(healthy_food)
# print(len(healthy_food)) # to check the length of the list
# print(type(healthy_food)) # to check the type of the list
# print(healthy_food[-2],)

#Accesing list items
#list items are indexed and you can access them by referring to the index number.
#Remember that the first item has index 0.
# print(healthy_fruits[0]) # Access the first item
# print(healthy_fruits[1]) # Access the second item
# print(healthy_fruits[2])   # Access the third item
# print(healthy_fruits[-1]) #last
# print(healthy_fruits[-3])

#Slicing

# cars = ["toyota","honda","BYD","BMW","Nissan","Audi","Ford"]
# print(cars)
# print(cars[0:4])
# print(cars[-4:-1])
# print(cars[2:])
# print(cars[:3])
# print(cars[:-3])

# # Modify List Items
# # You can change the value of a specific item by referring to its index number.
# cars[5] = "Mercedes Benz"
# print(cars)


# # How to add items to the end of a list
# cars.append("Gwagon")
# print(cars)

# # How to add items to a specific index in a list
# cars.insert(1, "Lexus")
# print(cars)

# # How to remove items from a list
# cars.remove("Nissan")
# print(cars)

# # How to remove an item at a specific index
# cars.pop(2)
# print(cars)

# # How to remove an entire list
# del cars
# print(cars)

# # How to clear a list
# cars.clear()
# print(cars)

#Tuples in Python: Tuples are used to store multiple items in a single variable.
#Tuples are one of 4 built-in data types in Python used to store collections of
#data, the other 3 are List, Set, and Dictionary, all with different qualities and 
# usage. Tuples are written with round brackets. ()
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0],
#the second item has index [1] etc.
#When we say that tuples are ordered, it means that the items have a defined order,
#and that order will not change.
#If you add new items to a tuple, the new items will be placed at the end of the tuple.
#The tuple is unchangeable, meaning that we cannot change,
#add, or remove items in a tuple after it has been created."""


# sneakers = ("Nike", "Adidas", "Puma","," "Reebok", "Vans")
# print(sneakers)
# print(type(sneakers))
# print(len(sneakers))


# # accessing tuple items
# print(sneakers[0])  # access the  first item
# print(sneakers[-5])  # access the third item




# still on tuples, but will add the input function to take user input
# store it in variable in a tuple format 
# shoe = input(str("Enter your sneakers brand: "))
# print(shoe)
# sneakers = input(str("Enter your sneakers brand: "))
# print(sneakers)
# boot = input(str("Enter your boots brand: "))
# print(boot)



# slices of  tuples
# print(sneakers[0:3])
# print(sneakers[-4:-1])

# modify tuple items
# Tuples are unchangeable, so you cannot change, add, or remove items once
# the tuple is created. But you can convert the tuple into a list,
# #however, make your changes, and convert it back into a tuple.
# sneakers["NIKE"] = "New Balance"
# print(sneakers)

# After convert the tuple into a list to be able to change it
# sneakers = list(sneakers)
# print(sneakers)
# sneakers[5] = "New Balance"
# print(sneakers)
# sneakers = tuple(sneakers)
# print(sneakers)



# 1
Playlist  = ["Band 4 Band ","Nobody has to know ","Between the bars ","Farewell","Cant STOP"]

# 2
top_artists = ("Lil Baby", "Kranium", "elliott Smith", "J.COLE")

# 3
my_music = [Playlist, top_artists]

# 4
print(len(my_music))

# 5
print(Playlist[2])

# 6
Playlist[0] = "Perfect"

#7
Playlist.append("Blinding Lights")

# 8
print(Playlist)
