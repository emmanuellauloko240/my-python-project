#LIST

#fruits = ["apple", "banana", "mango", "orange"]
#fruits.append('pineapple')
#fruits.remove("orange")
#print(fruits)
# def favorite_list():
#     favorite = ["ice-cream", "pizza", "shawarma","suya"]
#     favorite.pop(1)
#     favorite.pop()
#     favorite[1] = "burger"
#     favorite.append("exotic")
#     favorite.remove("exotic")

#     return favorite
# print(favorite_list())

# try it yourself from python crash

bicycles = ['trek', 'cannondale','redline','specialized']
message = "my first bicycle was a " + bicycles[0].title() +"."
print(message)

names = ['Enayi', 'mama', 'Enenu', 'ochanya']
print(names[0])
print(names[1])
print(names[-2])
print(names[-1])

name = "Enayi"
greetings = "greetings " + name 
print(greetings)

favorite_mode = "Honda motorcycle"
message = "i would like to own a " + favorite_mode
print(message.title())

# how to change an item value

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For
# example, you can start with an empty list and then add items to the list
# using a series of append() statements. Using an empty list, let’s add the elements 'honda', 'yamaha', and 'suzuki' to the list:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert()
# method. You do this by specifying the index of the new element and the
# value of the new item.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can
# use the del statement.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)