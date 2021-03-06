from tkinter import Canvas, Tk
import random
import time
import creature
import utilities

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

active_tag = None
MOUSE_CLICK = '<Button-1>'
MOUSE_DRAG = '<B1-Motion>'
palette = ('#f0a202', '#f18805', '#f0a202', '#d95d39', '#7b9e89')
counter = 6

creature.make_creature(canvas, (200, 200), size=150, tag='creature_1', fill='#f0a202')
creature.make_creature(canvas, (100, 400), size=50, tag='creature_2', fill='#f18805')
creature.make_creature(canvas, (50, 400), size=75, tag='creature_3', fill='#f0a202')
creature.make_creature(canvas, (400, 100), size=250, tag='creature_4', fill='#d95d39')
creature.make_creature(canvas, (350, 350), size=150, tag='creature_5', fill='#7b9e89')
counter = 6
def spawn_creature(event):
    global counter
    creature.make_creature(
        canvas, 
        (event.x, event.y), 
        size=random.randint(50, 150), 
        tag='creature_' + str(counter), # give each creature a unique tag
        fill=random.choice(palette)
    )
    counter += 1


canvas.bind(MOUSE_CLICK, spawn_creature)
canvas.bind(MOUSE_DRAG, spawn_creature)

while True:
    utilities.update_position_by_tag(canvas, 'creature_1', x=2, y=1)
    utilities.update_position_by_tag(canvas, 'creature_4', x=-4, y=0)
    gui.update()
    time.sleep(0.01)


########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()