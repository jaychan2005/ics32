#lab4.py

# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Jay Chan
# jayc10@uci.edu
# 54907952

import random

"""
The default numbers here are generally good enough to create a rich tree. 
You are free to play with the numbers if you want. Lower numbers will simplify the results, 
larger numbers will take more time to render and create hundreds of acorns.
"""

TREE_DEPTH = 5
NODE_DEPTH = 5

def tree_builder(nodes:list, level:int, acorn:str) -> list:
    """
    Builds a tree using the random integers selected from the tree_depth and node_depth defaults
    """
    r = random.randrange(1, NODE_DEPTH)
    for i in range(r):
        if level < TREE_DEPTH:
            level_id  = f"L{level}-{i}"
            if level_id == acorn:
                level_id += "(acorn)"
            n = [level_id]
            nodes.append(tree_builder(n, level+1, acorn_placer()))

    return nodes

def acorn_placer() -> str:
    """
    Returns a random acorn location based on tree_depth and node_depth defaults
    """
    return f"L{random.randrange(1,TREE_DEPTH)}-{random.randrange(1,NODE_DEPTH)}"

def run():
    # create a tree and start placing acorns
    tree = tree_builder([], 1, acorn_placer())
    
    # insert your solution code here
    routes = acorn_finder(tree, "", [])
    if count == 1:
        print(f"You have 1 acorn on your tree!")
    else:
        print(f"You have {count} acorns on your tree!")
    if count == 0:
        pass
    else:
        print("They are located on the following branches:")
    for route in routes:
        print(route)
    # end solution


def acorn_finder(map, routes, output):
    """
    Returns locations of acorns from tree.
    """
    global count 
        
    for level in map:
        if type(level) == list:
            if len(routes) == 0:
                routes += 'L0-0 -> '
                routes += str(level[0])
            else:
                if str((level[0])[4:]) == '(acorn)':
                    routes += (' -> ' + str((level[0])[:4]))
                else:
                    routes += (' -> ' + str(level[0]))
            acorn_finder(level, routes, output)
        else:
            if level[4:] == '(acorn)':
                count += 1
                output.append(routes)
    
    return output


if __name__ == "__main__":
    print("Welcome to PyAcornFinder! \n")
    count = 0
    run()
