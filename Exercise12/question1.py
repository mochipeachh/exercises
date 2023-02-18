cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# seeing what it prints out
# print(cheese)
# what's wrong with it: it prints out each char as a string
# a possible solution: to add 'oke' into the list using insert method, append is also viable
cheese.insert(3, 'Oke')

# adding 2 new items into the list with 1 command
# a possible solution: use the extend method
cheese.extend(['gouda, parmesan'])
print(cheese)
