from turtle import *
speed(1000)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange',]
number = raw_input('choose a number between 1 and 10: ')
if number == "1":
  # for loop for drawing left(150)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(150)
elif number == "2":
  # for loop for drawing left(300)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(175)
​
elif number == "3":
  # for loop for drawing left(300)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(300)
        
elif number == "4":
  # for loop for drawing left(300)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(450)
    
elif number == "4":
  # for loop for drawing left(300)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(450)
  
elif number == "5":
  # for loop for drawing left(300)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(600)
​
elif number == "6":
  # for loop for drawing left(300)
  for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(750)