# Phylogenetic Analyses of Primate and Hominin Mitochondrial Data

_A small Python toolkit for constructing, querying, and visualizing phylogenetic trees using UPGMA clustering and Turtle graphics._

---

## Overview
This repository provides utilities to:
- Build rooted phylogenetic trees from a distance matrix using the UPGMA algorithm.
- Traverse and query binary tree structures (e.g., count leaves, find subtrees, list all nodes, find parent/descendants).
- Scale branch lengths at internal nodes.
- Render phylogenetic trees (with proportional branch lengths) to the screen via Turtle graphics.
- Draw simple fractal trees and basic geometric shapes (for educational purposes).

Three main scripts are included:
- `groodies_phylo_tree.py`
  - Implements UPGMA clustering and tree-traversal utilities for binary trees.
- `turtle_tree_visualizations.py`
  - Defines Turtle graphics functions to draw squares, fractal trees, and phylogenetic-style trees with customizable branch lengths and angles.
- `upgma_turtle_viz.py`
    - Demonstrates how to:
        - Load predefined distance data for various taxa sets.
        - Run UPGMA clustering to build a rooted tree.
        - Scale branch lengths proportionally to root-to-leaf distances.
        - Render the resulting tree on a Turtle canvas.
- `mitodata.py`
    - Contains predefined distance data for various taxa.

---

## Repository Structure

    Phylogenetic-Tree-Toolkit/
    
    ├── groodies_phylo_tree.py          # Tree-building & traversal utilities (UPGMA, node queries, scaling)
    
    ├── turtle_tree_visualizations.py   # Turtle graphics functions for drawing trees (and other shapes)
    
    ├── upgma_turtle_viz.py             # Main demonstration: import data, run UPGMA, and visualize the tree
    
    ├── mitodata.py                     # Distance data for various taxa utilized for tree-building
    
    ├── Output_Trees                    # Phylogenetic trees created via turtle module
    
        ├── treeFrogs.png               # Tree frog tree
        
        ├── carnivores.png              # Carnivore tree
        
        ├── neandScaled.png             # Scaled homonim tree
        
        └── humanScaled.png             # Scaled human tree
    
    └── README.md                       # This file

---

## Prerequisites

- **Python 3.8+**
- The built-in `turtle` module (usually included with most Python installations)
- (Optional) Any standard text editor or IDE to view and modify the scripts

No additional third-party libraries are required.

---

## Installation

1. Clone or download this repository to your local machine (via bash):

       git clone https://github.com/<achandrasek6>/Phylogenetic-Tree-Toolkit.git
       cd Phylogenetic-Tree-Toolkit

2. Ensure your Python interpreter can import the built-in `turtle` module.
(Most Python installations include `turtle` by default.)

---

## Usage

### 1. Tree Building & Traversal: `groodies_phylo_tree.py`

This script provides core functions to manipulate and query binary tree structures, including:

- `upgma(speciesList, Distances)`
    - Builds a rooted tree using the UPGMA algorithm from a list of taxa (speciesList) and a distance dictionary (Distances).
- `leafCount(Tree)`
    - Returns the number of leaves in a given binary tree.
- `find(node, Tree)`
    - Checks if a specified node is present anywhere in the tree.
- `subtree(node, Tree)`
  - Returns the subtree rooted at a specified node (or None if that node is not found).
- `nodeList(Tree)`
  - Returns a flat list of all node labels (internal and leaf) in the tree.
- `descendantNodes(node, Tree)`
  - Returns all descendant node labels of a given node (excluding the node itself).
- `parent(node, Tree)`
  - Returns the parent label of a given node (or None if the node is the root or not found).
- `scale(Tree, scaleFactor)`
  - Multiplies every internal-node numeric value (branch length) in the tree by scaleFactor, producing a new scaled tree.
 
The bottom of `groodies_phylo_tree.py` contains example invocations demonstrating each function on a small toy tree. To experiment interactively:

    python3 groodies_phylo_tree.py

You will see printed outputs such as leaf counts, subtree extractions, node lists, descendant lists, parent relationships, and scaled tree structures.

### 2. Turtle-Based Visualizations: `turtle_tree_visualizations.py`

This module defines functions to render simple geometric shapes, fractal trees, and phylogenetic trees using Python’s `turtle` graphics API. Available functions include:

- `square(sideLength)`
    - Draws a square of the specified side length.
- `fractalTree2(angle, scale, trunkLength, levels)`
  - Recursively draws a fractal (binary) tree.
    - angle: angle between branches (in degrees)
    - scale: fractional scale factor for each sub-branch
    - trunkLength: initial trunk length
    - levels: recursion depth
- `drawPhyloTree(myTree)`
  - Renders a basic rooted binary tree assuming fixed branch lengths of 100 units per level. Nodes are labeled based on the tuple structure.
- `drawPhyloTree2(myTree, scale)`
  - Renders a phylogenetic tree where internal node values represent branch lengths. Branch lengths are scaled by scale and adjusted to draw proportional trees.
    - Requires that myTree is a 3-tuple of the form (value, left_subtree, right_subtree), where internal nodes have numeric values and leaves have string labels.
- `drawPhyloTree3(myTree, angle, scale)`
    - Similar to drawPhyloTree2, but uses a user-defined angle (in degrees) for left vs. right branches and trigonometric calculations to position branches correctly.

Each function can be tested by uncommenting the sample calls/test cases. For proper `turtle` drawing functionality, ensure only one function-`turtle.done()` pair is active.

To launch any of these visualizations, simply run the script with the relevant function call uncommented:

      python3 turtle_tree_visualizations.py

This will open a Turtle graphics window and draw the specified shape/tree. Close the window to return to the console.

### 3. UPGMA + Turtle Visualization Demo: `upgma_turtle_viz.py`

1. This is the main demonstration script that ties everything together:
2. Import the UPGMA & tree utilities from `groodies_phylo_tree.py`.
3. Import Turtle-based drawing functions from `turtle_tree_visualizations.py`.
4. Load predefined distance data for various taxa (e.g., Neanderthals vs. modern humans) from `mitoData.py`.
5. Run the UPGMA algorithm on each taxa set to build a rooted tree.
6. Scale branch lengths so that the root-to-leaf distance for a reference tree is normalized (e.g., scaled to 6 units).
7. Visualize the scaled tree using `drawPhyloTree2`, which displays a proportional phylogenetic tree on a Turtle canvas.

Example usage:

    python3 upgma_turtle_viz.py

You should see:
- Printed species lists and distance dictionaries in the console (for debugging/demonstration).
- A Turtle window pop up, rendering the scaled phylogenetic tree for the chosen taxa set.

---

## Troubleshooting

- **Turtle Window Does Not Appear / Freezes**
  - Ensure you are not running the script inside an environment that captures stdout and does not support interactive GUI (e.g., some remote terminals).
  - Run in a local Python environment or IDE that allows GUI windows.
- **ModuleNotFoundError when importing turtle**
  - Confirm that you are using a standard Python distribution (CPython). Some minimal or embedded installations omit the turtle module.
  - If using a virtual environment, ensure it was created from a full Python installation.
- **Branch Lengths Seem Too Large / Too Small**
  - Adjust the scale argument passed to `drawPhyloTree2` or `drawPhyloTree3` to change the visual proportions.
  - The constant `CORRECTION` in `turtle_tree_visualizations.py` (≈ 1.155) helps correct for the diagonal drawing angle; you may fine-tune it based on your screen resolution or desired appearance.
- **Slow Performance on Large Trees**
  - Both UPGMA clustering (which is O(n²) in the number of taxa) and Turtle graphics (which draws each branch sequentially) can become slow for very large datasets.
  - For large distance matrices (> 100 taxa), consider downsampling, using optimized clustering libraries (e.g., `SciPy`’s linkage), or drawing a simplified tree.


