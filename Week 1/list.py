# lists are like arrays in javascript
fruits = ['apple','orange','watermelon','grapefruit']

print(fruits)

print(fruits[2])

# add 'pear' to the end of fruits
fruits.append('pear')

print(fruits)

# counts item 'apple' in the list
print( fruits.count('apple') )

# gives you the length of the list
print( len(fruits) )

#delete an item from a list - item with index 1 ('orange')
del fruits[1]
print(fruits)
