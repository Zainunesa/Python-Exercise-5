# # Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ['apple','banana','pear','strawberry']
# TODO: Add a fruit to the end of the list

fruits.append("avo")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, 'orange')
# fruits = ["orange"] + fruits
# TODO: Remove a fruit from the list
fruits.remove("banana")

# # TODO: Print the modified list
print(fruits)
#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]

# TODO: Create a new list with each number squared
square_number = [1,4,9,16,25]
# TODO: Find the sum and average of the original numbers
number_sum = sum(numbers)
Average = number_sum/len(numbers)
# TODO: Print the results
print(Average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# # TODO: Create a dictionary of countries and their capitals
world = {
  "South Africa": "Pretoria",
  "New Zealand" : "Wellington",
  "Germany"     : "Berlin"
}
# # TODO: Add a new country-capital pair
World = {
  "South Africa": "Pretoria",
  "New Zealand" : "Wellington",
  "Germany"     : "Berlin"
}
world.update({"England": "London"})
# # TODO: Update the capital of an existing country
World = {
  "South Africa": "Pretoria",
  "New Zealand" : "Wellington",
  "Germany"     : "Berlin"
}
world.update({"South Africa": "Cape Town"})
print(world)
# # TODO: Remove a country-capital pair
World = {
  "South Africa": "Pretoria",
  "New Zealand" : "Wellington",
  "Germany"     : "Berlin"
}
world.pop("Germany")
# # TODO: Print the modified dictionary
print(world)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "Apple": "Green",
    "Pear"  : "Yellow",
    "Strawberry": "Red"
}
# TODO: Print all the fruits (keys)
# for key in fruit_colors:
#     print(key)
print(fruit_colors.keys())
# TODO: Print all the colors (values)
# for values in fruit_colors.values():
#     print(values)
print(fruit_colors.values())
# # for value in fruit_colors:
# # print(key)
# # TODO: Print each fruit and its color
f = fruit_colors.items()

print(f)
# TODO: Check if a fruit is in the dictionary and print its color
fruit = "Apple"

if fruit in fruit_colors:
    print(f"{fruit} color is: {fruit_colors[fruit]}")
else:
    print(f"{fruit} is not in the dictionary")