# This script will ask the user for its username, by using the raw_input function. 
# Then a list of allowed users is created named user1 and user2. 
# The control statement checks if the input from the user matches the ones that are in the allowed users list.


#!/usr/bin/env python

#get the username from a prompt
username = raw_input("Login: >> ")

#list of allowed users
user1 = "Jack"
user2 = "Jill"

#control that the user belongs to the list of allowed users
if username == user1:
    print "Access granted"
elif username == user2:
    print "Welcome to the system"
else:
    print "Access denied"
	