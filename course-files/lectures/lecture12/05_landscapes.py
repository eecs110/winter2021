from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Landscapes')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

palette = ['#ebbab9', '#c9c5ba', '#97b1a6', '#698996', '#407076']
'''
Challenge: 
1. Modify this program so that each time you run it, it draws a
   circle with a random position, size, and color. 
2. Make 20 circles w/random positions, sizes, and colors.
3. Make 1,000 circles
4. Make them twinkle
'''
shapes.make_circle(canvas, (250, 250), 30, color=palette[0], tag='circle')


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()