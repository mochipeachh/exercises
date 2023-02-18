tup = 'hello'
print(len(tup))
# prints 5
# what's happening here?
# it's printing out the number of characters in the string 'hello'


tup = 'hello',
print(len(tup))
# prints 1
# what's happening here?
# it's counting the number of values within the tuple instead of the length due to the trailing comma
# that comma tells the computer to expect more values
