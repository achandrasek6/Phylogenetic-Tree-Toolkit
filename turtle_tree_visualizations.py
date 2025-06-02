"""
turtle_tree_visualizations.py

A collection of Turtle graphics functions for drawing geometric shapes,
fractal trees, and phylogenetic‐style trees with customizable branch lengths
and angles.

Functions included:
  - square(sideLength): Draws a simple square.
  - fractalTree2(angle, scale, trunkLength, levels):
      Recursively draws a fractal tree.
  - drawPhyloTree(myTree):
      Renders a basic binary tree structure with fixed branch lengths.
  - drawPhyloTree2(myTree, scale):
      Renders a binary tree with branch lengths proportional to numeric node values.
  - drawPhyloTree3(myTree, angle, scale):
      Like drawPhyloTree2 but uses trigonometry to adjust branch lengths for a given angle.

Example usage:
    from turtle_tree_visualizations import drawPhyloTree2
    drawPhyloTree2(myPhyloTree, 30)
    turtle.done()
"""

import turtle

screen = turtle.Screen()
screen.title("Turtle Visualization")

# Square
def square(sideLength):
    """Draws a square of side length sideLength"""
    for num in range(4):
        turtle.forward(sideLength)
        turtle.left(90)
    turtle.done()

# Sample call
#square(250)

def fractalTree2(angle, scale, trunkLength, levels):
    """Draws a fractal tree with the specified parameters"""
    if levels == 0: return
    else:
        turtle.forward(trunkLength)
        turtle.left(angle)
        fractalTree2(angle, scale, trunkLength * scale, levels - 1)
        turtle.right(2 * angle)
        fractalTree2(angle, scale, trunkLength * scale, levels - 1)
        turtle.left(angle)
        turtle.backward(trunkLength)

#fractalTree2(45, 0.75, 100, 4)
#turtle.done()

# Simple tree
myTree = ("A",
              ("B",
                   ("C", (), ()),
                   ("D", (), ())
              ),
              ("E", (), ())
         )

def drawPhyloTree(myTree):
    """Function to draw phylogenetic tree using turtle graphics"""
    if myTree:
        root, left, right = myTree

        # Label current root
        turtle.write(root)

        # Draw the left subtree
        if left:
            turtle.left(45)
            turtle.forward(100)
            turtle.right(45)
            drawPhyloTree(left)
            turtle.left(45)
            turtle.backward(100)
            turtle.right(45)

        # Draw the right subtree
        if right:
            turtle.right(45)
            turtle.forward(100)
            turtle.left(45)
            drawPhyloTree(right)
            turtle.right(45)
            turtle.backward(100)
            turtle.left(45)


#drawPhyloTree(myTree)
#turtle.done()

# Varying branch lengths
ANGLE = 30
CORRECTION = 1.155

myTree = (5,
              (3,
                   ("A", (), ()),
                   ("B", (), ())
              ),
              ("C", (), ())
         )

def drawPhyloTree2(myTree, scale):
    """Draws a phylogenetic tree with varying branch lengths using turtle graphics."""
    if myTree:
        root, left, right = myTree

        # Write the current root label
        # Check if root is a number
        if isinstance(root, (int, float)):
            # Write the rounded numeric value
            turtle.write(f"{root:.3f}", align="center", font=("Arial", 12, "normal"))
        else:
            # Write the word "root" if root is not a number
            turtle.write(root, align="center", font=("Arial", 12, "normal"))

        # Draw the left subtree
        if left and isinstance(root, (int, float)): # Ensure root is numeric
            # Ensure left[0] is numeric before subtraction
            left_height = root - (left[0] if isinstance(left[0], (int, float)) else 0)
            turtle.left(ANGLE)
            turtle.forward(left_height * scale * CORRECTION)
            turtle.right(ANGLE)
            drawPhyloTree2(left, scale)
            turtle.left(ANGLE)
            turtle.backward(left_height * scale * CORRECTION)
            turtle.right(ANGLE)

        # Draw the right subtree
        if right and isinstance(root, (int, float)): # Ensure root is numeric
            # Ensure right[0] is numeric before subtraction
            right_height = root - (right[0] if isinstance(right[0], (int, float)) else 0)
            turtle.right(ANGLE)
            turtle.forward(right_height * scale * CORRECTION)
            turtle.left(ANGLE)
            drawPhyloTree2(right, scale)
            turtle.right(ANGLE)
            turtle.backward(right_height * scale * CORRECTION)
            turtle.left(ANGLE)


#drawPhyloTree2(myTree, 30)
#turtle.done()

# Custom branch angles
import math

def drawPhyloTree3(myTree, angle, scale):
    """Draws a phylogenetic tree with varying branch lengths and customizable angles using turtle graphics."""
    if myTree:
        root, left, right = myTree

        # Write the current root label
        turtle.write(str(root), align="center", font=("Arial", 12, "normal"))

        # Draw the left subtree
        if left and isinstance(root, (int, float)):
            left_height = root - (left[0] if isinstance(left[0], (int, float)) else 0)  # Difference in height
            branch_length = (left_height * scale) / math.cos(math.radians(angle))
            turtle.left(angle)
            turtle.forward(branch_length)
            turtle.right(angle)
            drawPhyloTree3(left, angle, scale)
            turtle.left(angle)
            turtle.backward(branch_length)
            turtle.right(angle)

        # Draw the right subtree
        if right and isinstance(root, (int, float)):
            right_height = root - (right[0] if isinstance(right[0], (int, float)) else 0)
            branch_length = (right_height * scale) / math.cos(math.radians(angle))
            turtle.right(angle)
            turtle.forward(branch_length)
            turtle.left(angle)
            drawPhyloTree3(right, angle, scale)
            turtle.right(angle)
            turtle.backward(branch_length)
            turtle.left(angle)

#drawPhyloTree3(myTree, 30, 30)
#turtle.done()

# Tree frogs solution
treeFrogs = (64,
             (60,
              (57,
               (54,
                (35,
                 (5,
                  ('Hyla versicolor',(), ()),
                  ('Hyla avivoca',(),()) ),
                 (20,
                  ('Triprion petasatus',(), ()),
                  ('Anotheca spinosa',(),()) )
                 ),
                ('Tepuihyla edelcae',(),())),
               ('Dendropsophus marmoratus',(),()) ),
              ('Hyloscirtus armatus',(),())),
             ('Phyllomedusa tarsius',(),()))

#drawPhyloTree3(treeFrogs, 30, 10)
#turtle.done()

# Common ancestor of tree frogs likely lived in Tropical South America