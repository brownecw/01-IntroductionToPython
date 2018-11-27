"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Colin Browne.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

window.tracer(1)

jeff = rg.SimpleTurtle('turtle')

jeff.pen = rg.Pen("red", 4)

jeff.speed = 60

for k in range(40):
    jeff.right(90)
    jeff.draw_regular_polygon(3,10 + k)
    jeff.forward(k*10)
window.tracer(1)
steve = rg.SimpleTurtle('turtle')
steve.pen = rg.Pen("black",6)

steve.speed = 45

for k in range(60):
    steve.right(45)
    steve.forward(k*4)

window.close_on_mouse_click()