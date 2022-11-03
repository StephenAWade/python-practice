# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

#Get value
# print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delet tuple
del fruits2

print(len(fruits))




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# check if something is in a set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
# fruits_set.clear()

# Delete
# del fruits_set

print(fruits_set)