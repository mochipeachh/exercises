# using a set as the question specified unique random numbers and sets dont allow duplicate elements
import random
myset=set()

for x in range(6):
    lotto = random.randint(1, 50)
    myset.add(lotto)
    print(myset)

while len(myset)<6:

    lotto = random.randint(1, 50)
    myset.add(lotto)
    print(myset)





