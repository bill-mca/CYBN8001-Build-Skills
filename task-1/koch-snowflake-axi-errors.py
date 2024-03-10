import axi

# To Do:
#  - Setup sys.argv so that the user can specify the global variables from the
#    Command line.
#  - Split into two specialised scripts. one to generate a vector image of a
#    Koch Snowflake and the other to print the specified vector image with the
#    Pen plotter.

# Global variables specifying the size of different sheets of paper.
# Units here are inches.
A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds

# The BOUNDS global variable is called by the main function to scale the drawing
# to size.
BOUNDS = A4_PORT

# Set this variable to true when you wish to draw with the plotter.
draw = False

def side(t, levels, length):
  """
  This function draws one side of the famous fractal the Koch Snowflake.

  Note that this function does not raise or lower the turtle object's pen. It
  finishes with the same orientation that it started with but having advanced
  forward by the specified length.

    Parameters
    ----------
    t : Turtle object
      An active instance of the turtle class that will be called to draw the
      snowflake.
    levels : int
      An iteger indicating the desired depth of recursion for the fractal.
      larger numbers indicate more iteration. For example levels=0 just draws an
      equilateral triangle.
    length: int
      The stright-line length of the from start point to end point. Expressed in
      the units set for the turtle object which are pixels by default.

    Returns
    ----------
    This function does not return anything.

  """
  # This function uses functional recursion. It calls itself many times with
  # slightly different arguments each time to produce a complex, chevron shaped
  # component of the Koch Snowflake fractal.
  # The md variale is set to avoid recalculating it several times. It is the
  # length of sides in the next deepest level of iteration.
  md = length/3
  # If this is the lowest level of iteration: draw a straight line
  if levels == 0:
    t.forward(length)
  # Here's the functional recursion.
  # Else, draw 3 sides of a Koch Snowflake at one level of iteration deeper than
  # the current iteration.
  # Orient the sides in a cevron shape.
  # Make the sides all the same length.
  else:
    side(t, levels-1, length/3)
    t.left(60)
    side(t, levels-1, md)
    t.right(120)
    side(t, levels-1, md)
    t.left(60)
    side(t, levels-1, md)

def koch(t, levels, length):
  """
  This function draws the famous fractal the Koch Snowflake.

  Note that this function does not raise or lower the turtle object's pen. It
  finishes in the same location and orientation that it started in.

    Parameters
    ----------
    t : Turtle object
      An active instance of the turtle class that will be called to draw the
      snowflake.
    levels : int
      An iteger indicating the desired depth of recursion for the fractal.
      larger numbers indicate more iteration. For example levels=0 just draws an
      equilateral triangle.
    length: int
      The stright-line length of the from start point to end point of one side
      of the snowflake. Expressed in the units set for the turtle object which
      are pixels by default.

    Returns
    ----------
    This function does not return anything.

  """
  # All the hard work for this function is done by the side function defined
  # above. This function simply draws one side, turns 120 degrees, draws a
  # second side, turns 180 degrees and draws the third side. It turns 120
  # degrees as the last step so that it finishes back in start location with the
  # same orientation.
	side(t, levels, length)
	t.right(120)
	side(t, levels, length)
	t.right(120)
	side(t, levels, length)
	t.right(120)

if __name__ == '__main__':
  # If this script is being called from the command line run the following code:

  # Initialise the turtle object with default settings.
  t = axi.Turtle()

  # Use an arbitrary large integer as the side length. Due to the scaling
  # applied below this number has little effect.
  # I suspect that one of the upstream methods truncates decimal numbers into
  # integers and that this is the cause of imprecise graphing when small values
  # are used for side_length.
  # with a small value for side_length:
  #   ((((side_length//3)//3)//3)//3) * pow(3, 4) != side_length
  side_length = 10

  # Calling the snowflake algorithm many times draws the high levels of
  # iteration over the top of deeper levels.
  koch(t, 0, side_length)
  koch(t, 1, side_length)
  koch(t, 2, side_length)
  koch(t, 3, side_length)
  koch(t, 4, side_length)
  koch(t, 5, side_length)
  koch(t, 6, side_length)
  koch(t, 7, side_length)

  # This line of code came from upstream. It is the most important line for
  # compatibility with the axi draw. Takes your drawing in arbitrary units and
  # rescales it so that the axi draw can plot it on a page. The axi draw expects
  # coordinates with units in inches and has a maximum drawing size of about A3.
  drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3],
    step=90, padding=0.5)
  # Render drawing to a drawing to a d
  im = drawing.render()
  # Create an image file of the drawing
  im.write_to_png('koch-snowflake-errors.png')
  #im.svg_dump('koch-snowflake-errors.svg')

  # Draw a physical drawing with the plotter if the user has specified that they
  # want it drawn by setting draw = True
  if draw:
    axi.draw(drawing)
