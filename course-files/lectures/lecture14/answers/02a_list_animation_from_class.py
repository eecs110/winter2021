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

for i in range(1, 101):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    r = random.randint(5, 25)
    tag_name = 'circle' + str(i)
    utilities.make_circle(canvas, (x, y), r, color=None, tag=tag_name)


while True:
    for i in range(1, 101):
        utilities.move(canvas, 'circle' + str(i), x=0, y=1)
    gui.update()
    time.sleep(.001)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
