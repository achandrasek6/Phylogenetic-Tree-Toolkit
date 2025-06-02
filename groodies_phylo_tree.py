"""
groodies_phylo_tree.py

Provides a toolkit for constructing, querying, and visualizing binary tree structures:
  - Implements UPGMA clustering (findClosestPair, updateDist, upgma) to build rooted trees from a distance matrix.
  - Offers tree‐traversal utilities (leafCount, find, subtree, nodeList, descendantNodes, parent).
  - Supports branch‐length scaling (scale).
  - Renders phylogenetic trees to screen using turtle graphics (drawPhyloTree2).
"""

Groodies = ("X",
                ("Y",
                    ("W", (), ()),
                    ("Z",
                        ("E", (), ()),
                        ("L", (), ())
                    )
                ),
                ("C", (), () )
            )

def leafCount(Tree):
    '''Finds the number of leaves in a tree'''
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]

    if Subtree1 == (): return 1 # Base case; it's a leaf
    else: return leafCount(Subtree1) + leafCount(Subtree2) # recursive case

# Test cases
#print(leafCount(Groodies))
# 4
#print(leafCount((5,(3,("A", (), ()),("B", (), ())),("C", (), ()))))
# 3

def find(node, Tree):
    '''Returns True if the given node is in the given Tree and returns False otherwise'''
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]

    if Subtree1 == () or Subtree2 == (): return False # terminal node
    elif node in Subtree1 or node in Subtree2: return True # if node is in either subtree there is a match
    else: return find(node, Subtree1) or find(node, Subtree2) # recursive case; keep searching

#print(find('W',Groodies))
# True
#print(find('A',Groodies))
# False
#print(find('E',Groodies))
# True

def subtree(node, Tree):
    '''Returns the subtree of the given Tree rooted at the given node'''
    if not Tree:
        return # invalid input
    root = Tree[0]
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]

    if root == node: return Tree # base case; match
    sub_tree1_result = subtree(node, Subtree1)
    # check to see if Subtree1 exists
    if sub_tree1_result:
        return sub_tree1_result # if it exists, recursively search it
    return subtree(node, Subtree2) # if it doesn't exist, search Subtree2

#print(subtree("W", Groodies))
# ('W', (), ())
#print(subtree("Y", Groodies))
# ('Y', ('W', (), ()), ('Z', ('E', (), ()), ('L', (), ())))
#print(subtree("Z", Groodies))
# ('Z', ('E', (), ()), ('L', (), ()))

def nodeList(Tree):
    '''Takes a Tree as input and returns a list of all the nodes in that tree
    (including both leaves and ancestral nodes)'''
    root = Tree[0]
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    if Subtree1 == (): return [root] # base case; end of search path; add root to list
    elif Subtree1: return [root] + nodeList(Subtree1) + nodeList(Subtree2) # if Subtree1 is not final node, keep searching

# Test case
#print(nodeList(Groodies))
# ['X', 'Y', 'W', 'Z', 'E', 'L', 'C']

def descendantNodes(node, Tree):
    '''Returns the list of all descendant nodes of the given node in the Tree'''
    root = Tree[0]
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]

    if node == root: return nodeList(Subtree1) + nodeList(Subtree2) # if node = root, return combined nodelist of child trees
    subtree_node = subtree(node, Tree)
    if subtree_node: # if subtree exists
        return nodeList(subtree_node[1]) + nodeList(subtree_node[2]) # don't want to return root

# Test cases
#print(descendantNodes("X", Groodies))
# ['Y', 'W', 'Z', 'E', 'L', 'C']
#print(descendantNodes("Y", Groodies))
#  ['W', 'Z', 'E', 'L']
#print(descendantNodes("Z", Groodies))
# ['E', 'L']

def parent(node, Tree):
    '''Returns the parent of the given node in the Tree'''
    '''If the node has no parent in the tree, the function should return the special value None'''
    if not Tree or Tree == ():
        return None  # Invalid input or empty tree

    root = Tree[0]
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]

    if node == root:
        return None  # Root node has no parent
    else:
        # Check if node is in the left subtree
        if node in Subtree1:
            return root
        # Check if node is in the right subtree
        elif node in Subtree2:
            return root
        else:
            # Recursively search for the node's parent in the subtrees
            left_result = parent(node, Subtree1)
            right_result = parent(node, Subtree2)
            if left_result:
                return left_result
            elif right_result:
                return right_result
            else:
                return None  # Node not found in either subtree

# Test cases
#print(parent("Y", Groodies))
# X
#print(parent("W", Groodies))
# Y
#print(parent("Z", Groodies))
# Y
#print(parent("E", Groodies))
# Z
#print(parent("X", Groodies))
# None
#print(parent("X", Groodies) == None)
# True

Tree = (4.3,
         ('C', (), ()),
         (3.2,
           ('A', (), ()),
           ('B', (), ()))
        )

def scale(Tree, scaleFactor):
    '''Takes a Tree as input, multiplies the numbers at its internal nodes by scaleFactor,
    and returns a new tree with those values'''

    if not Tree: # function finished in a branch if this point is reached in recursion; indicates terminal node
        return ()

    root = Tree[0]

    if type(root) in [int, float]:  # Only scale if root is a number
        scale_root = root * scaleFactor
    else:
        scale_root = root

    # Ensure that the subtrees exist before calling scale on them
    Subtree1 = scale(Tree[1], scaleFactor) if Tree[1] else ()
    Subtree2 = scale(Tree[2], scaleFactor) if Tree[2] else ()

    return (scale_root, Subtree1, Subtree2)

# Test case
#print(scale(Tree,2.0))
# (8.6, ('C', (), ()), (6.4, ('A', (), ()), ('B', (), ())))
