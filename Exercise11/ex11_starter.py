#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# initial print out of the length of the string
print(len(Belgium))

# Q: print a line of hyphens the length of the belgium string
print('-'*len(Belgium))

# Q: print the string with colons instead of commas
print(Belgium.replace(',', ':'))

# Q: adding the 2nd field with the 4th field
# turning the string into a list with commas
mylist = Belgium.split(',')
# printing the list
print(mylist)
#  printing the class type to make sure it is a list
print(type(mylist))
# turning field 2 and 4 into ints from strings and adding them
print(int(mylist[1])+int(mylist[3]))


