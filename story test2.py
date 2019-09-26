# let the user know what's going on
print ("Welcome to Deathlab                                                    !")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
character1 = raw_input("Enter a character you don't like: ")
color1 = raw_input("What is your favorite color?: ")
yourName = raw_input("What's your name?: ")
location1 = raw_input("Your favorite place: ")
object1 = raw_input("An object you like most: ")
food1 = raw_input("A food you had recently: ")
person = raw_input("Name of the person on your left: ")
adjective2 = raw_input("Enter one more unusual adjective: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "The dead " + character1 + " silently walking to " + yourName + " lucky " + location1 + ", " \
"crazyly biting " + object1 + " for the person on your left which has made by " + food1 + ". " \
"This is a " + adjective2 + " gift " + yourName + " ever had in whole life. " \
"" + yourName + " then goes back home in the midnight. " \
"The next rainny morning " + person + " is sitting in the middle of " + location1 + " " \
"with a knife in hand and looking at " + yourName + "."

# finally we print the story
print (story)