from tkinter import Canvas, Tk
import time
import utilities
import math
import random

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# 1. generate a list of rules that each bubble should follow:
data = []
for i in range(1, 101):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    r = random.randint(5, 25)
    speed = random.randint(1, 5)
    tag_name = 'circle' + str(i)
    bubble_rule = [x, y, r, speed, tag_name]
    data.append(bubble_rule)

# 2. use the data to generate 100 bubbles:
for bubble_rule in data:
    x = bubble_rule[0]
    y = bubble_rule[1]
    r = bubble_rule[2]
    speed = bubble_rule[3]
    tag_name = bubble_rule[4]
    utilities.make_circle(canvas, (x, y), r, color=None, tag=tag_name)


while True:
    for bubble_rule in data:
        speed = bubble_rule[3]
        tag_name = bubble_rule[4]
        utilities.move(canvas, tag_name, x=0, y=speed)
        top = utilities.get_top(canvas, tag_name)
        if top > 550:
            utilities.move(canvas, tag_name, x=0, y=-600)

    gui.update()
    time.sleep(.001)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
