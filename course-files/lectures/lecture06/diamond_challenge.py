from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=450, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
'''
1. Make a function called draw_diamond that always draws the same diamond 
   in the same spot. This function will require one required argument, canvas:Canvas. 
   When you're done, call the function to ensure that it works.

2. Modify the function so that it can draw a diamond ANYWHERE on the 
   screen (always of the same size), by:
      a) Adding a REQUIRED center:tuple parameter to the function signature, and
      b) Using the center parameter in the function body, in order to 
         calculate the coordinates of the diamond.
   When you’re done, call the function with several different center 
   arguments to ensure that it works.

3. Enhance the function again so that you can draw a diamond of any size by:
      a) Adding an OPTIONAL size:int=100 parameter to the function signature
        (which will give the diamond a default size of 100 pixels tall / wide.
      b) Incorporating the size parameter into your logic that determines 
         where the diamond should be drawn.
   When you’re done, call the function with several different center and 
   size arguments to ensure that it works. Also test that you can call your 
   function WITHOUT passing a size parameter (because it’s a 
   keyword / optional parameter).

4. Finally, further modify the function so that it allows the user to draw the diamond...
      * With any fill color
      * With any border color
      * With any border width

5. Challenge: Make a function that draws 4 diamonds positioned around a center 
   point (see drawing from lecture slides). 
      * Hint: in your draw_four_diamonds function, invoke the previous 
        draw_diamond function that you made, 4 times.
      * Just as before, make the border, color, etc customizable    

'''


canvas.create_polygon(
    [ 
        (300, 100), # top-most coordinate
        (400, 200), # right-most coordinate
        (300, 300), # bottom-most coordinate
        (200, 200)  # left-most coordinate
    ],
    fill='teal',
    width=5,
    outline='black',
    activefill='hotpink',
    activeoutline='#999999'
)


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()