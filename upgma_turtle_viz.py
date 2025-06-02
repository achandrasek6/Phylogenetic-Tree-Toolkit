"""
upgma_turtle_viz.py

Main script to construct and visualize UPGMA phylogenetic trees using Turtle graphics:

  – Imports distance data for multiple taxa sets (Neanderthals, humans, etc.).
  – Implements UPGMA clustering (findClosestPair, updateDist, upgma) to build rooted trees.
  – Scales branch lengths proportionally to root‐to‐leaf distances.
  – Renders the final tree via drawPhyloTree2 with customizable scaling.
  – Demonstrates visualization by drawing the scaled human phylogeny on a Turtle canvas.
"""

from turtle_tree_visualizations import drawPhyloTree2
from groodies_phylo_tree import leafCount, scale
from mitoData import neandList, neandMatrix, humansList, humansMatrix, groodiesList, groodiesMatrix, fitchList, \
    fitchMatrix, carnivoresList, carnivoresMatrix
import turtle

#print(neandList)
# [('Chimpanzee', (), ()), ('Neanderthal', (), ()), ('San', (), ()), ('Yoruba', (), ()), ('Finnish', (), ()), ('Kostenki', (), ())]
#print(neandMatrix)
# {(('San', (), ()), ('Neanderthal', (), ())): 0.012138, (('Neanderthal', (), ()), ('Neanderthal', (), ())): 0.0, ...
#print(humansList)
# [('San', (), ()), ('Kikuyu', (), ()), ('Yoruba', (), ()), ('Han', (), ()), ('Finnish', (), ()), ('Papuan', (), ())]
#print(humansMatrix)
# {(('Kikuyu', (), ()), ('Kikuyu', (), ())): 0.0, (('Finnish', (), ()), ('Papuan', (), ())): 0.001312, ...

def findClosestPair(speciesList, Distances):
    """Find the pair of trees in the speciesList with the least distance."""
    minDistance = float("inf")  # Initialize min distance to max possible value
    closestPair = None
    for species1 in speciesList:
        for species2 in speciesList:
            if species1 != species2:  # Exclude identical species
                # Safely check for distance entry
                distance = Distances.get((species1, species2), Distances.get((species2, species1)))
                if distance < minDistance:
                    minDistance = distance
                    closestPair = (species1, species2)
    return closestPair

# Test cases
#print(findClosestPair(neandList, neandMatrix))
# (('Finnish', (), ()), ('Kostenki', (), ()))
#print(findClosestPair(humansList, humansMatrix))
# (('Finnish', (), ()), ('Papuan', (), ()))

def updateDist(speciesList, Distances, newTree):
    """Update the Distances dictionary for the new cluster."""
    tree1, tree2 = newTree[1], newTree[2]
    leaf_total = leafCount(tree1) + leafCount(tree2)  # Total number of leaves
    for tree in speciesList:
        if tree != tree1 and tree != tree2:  # Don't update distances for merged trees
            # Safely retrieve distances
            dist1 = Distances.get((tree, tree1), Distances.get((tree1, tree)))
            dist2 = Distances.get((tree, tree2), Distances.get((tree2, tree)))

            # Calculate new distance for the cluster
            newDistance = (leafCount(tree1) / leaf_total * dist1) + (leafCount(tree2) / leaf_total * dist2)

            # Add to distances (both forward and reverse entries)
            Distances[(newTree, tree)] = newDistance
            Distances[(tree, newTree)] = newDistance


def upgma(speciesList, Distances):
    """This function takes as input the the speciesList and the distance dictionary and runs the algorithm.
    It repeatedly does the following until there is only one tree in the speciesList,
    at which point that phylogenetic tree is returned. """
    # Keep looping until final tree
    while len(speciesList) > 1:
        tree1, tree2 = findClosestPair(speciesList, Distances)
        distance = Distances.get((tree1, tree2), Distances.get((tree1, tree2))) / 2.0 # Div by 2 to calc evolutionary time
        newTree = (distance, tree1, tree2) # New tree node
        speciesList.remove(tree1) # Remove merged species from list
        speciesList.remove(tree2)
        updateDist(speciesList, Distances, newTree) # Calc distances between combined tree and other species/groups
        speciesList.append(newTree) # Add combined tree to species list
    # Return finalized tree
    return speciesList[0]

ANGLE = 30
CORRECTION = 1.155

fitchTree = upgma(fitchList, fitchMatrix)
#drawPhyloTree2(fitchTree, 35)
#turtle.done()

carnivoresTree=upgma(carnivoresList, carnivoresMatrix)
#drawPhyloTree2(carnivoresTree,6.5)
#turtle.done()

neandTree=upgma(neandList, neandMatrix)
humansTree=upgma(humansList, humansMatrix)
neandTreeScaled=scale(neandTree,6.0/neandTree[0])
humansTreeScaled=scale(humansTree,6.0/neandTree[0])

#drawPhyloTree2(neandTreeScaled, 140)
#turtle.done()

#drawPhyloTree2(humansTreeScaled, 2000)
#turtle.done()

# Supports out of Africa hypothesis