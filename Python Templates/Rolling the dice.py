# This script will ask the user for its username, by using the raw_input function. 
# Then a list of allowed users is created named user1 and user2. 
# The control statement checks if the input from the user matches the ones that are in the allowed users list.

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")
	