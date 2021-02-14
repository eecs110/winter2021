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

def spawn_creature(event):
    # global keyword used here because we're going to 
    # MODIFY the global variables above
    global active_tag
    global counter

    shape_tag = utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    # if shape_tag is None, it means that we haven't clicked on 
    # a creature so we can CREATE one:
    if not shape_tag:
        creature.make_creature(
            canvas, 
            (event.x, event.y), 
            size=random.randint(50, 150), 
            tag='creature_' + str(counter), # give each creature a unique tag
            fill=random.choice(palette)
        )
        counter += 1
    # otherwise, we'll SELECT the creature we just clicked on
    # so that it can be dragged (in the move_creature function):
    else:
        active_tag = shape_tag

def move_creature(event):
    if not active_tag:
        return
    center = utilities.get_center_coords(canvas, active_tag)
    
    # current x, y position:
    x = center[0]
    y = center[1]

    # changed x, y position:
    delta_x = -1 * (x - event.x)
    delta_y = -1 * (y - event.y)

    # update the screen:
    utilities.update_position_by_tag(canvas, active_tag, x=delta_x, y=delta_y)
    

canvas.bind(MOUSE_CLICK, spawn_creature)
canvas.bind(MOUSE_DRAG, move_creature)

while True:
    utilities.update_position_by_tag(canvas, 'creature_1', x=2, y=1)
    utilities.update_position_by_tag(canvas, 'creature_4', x=-4, y=0)
    gui.update()
    time.sleep(0.01)


########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()