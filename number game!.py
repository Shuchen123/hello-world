import random
celebrityList=["Donald Trump","Chris Hemsworth","Ben Affleck","Scarlett Johansson","Tom Marvolo Riddle","Tom Hiddleton"]
randCelebrity=random.randint(0,5)

print 'Hello Player'
print 'Guess a lucky number within 1-10 and you will be invited to dinner tonight of one secret celebrity'

expected_number = random.randint(1,10)

max_play_number = 3

current_play_number = 1

while current_play_number <= max_play_number:
 current_play_number+=1
 actual_numer = input()
 if actual_numer == expected_number:
  print 'Congratulations! '+celebrityList[randCelebrity]+' invites you to dinner!'+'\nSee you at 7pm tomorrow!'
  break
 else:
  if actual_numer > expected_number:
   print 'Sorry, please try again, the lucky number is smaller '
  else:
   print 'The lucky number is bigger'

print 'See you next time'