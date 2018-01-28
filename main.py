"""
@author Meghraj Bendre
@email bendre@usc.edu

Usage: python main.py
"""

#simple class for node manipulation
class Node:
    def __init__(self, player, state, parent=None):
        self.player = player
        self.state = state
        self.parent = parent    #keeps track of the parent
        self.children = []      #keeps track of the children for traversal

    def tree_creation(self, player, initial_state, parent):



#class to construct the game tree 
class Tree:
    def __init__(self):
        self.root = None

    def tree_creation(self, player, initial_state, parent):
        if self.root:
            return self.root.tree_creation(player, initial_state, parent)
        else:
            self.root = Node(player, initial_state, parent) 

#reads input file and does necessary formatting
def read_input_file():
    input_file = open("input.txt")
    ip = input_file.read().splitlines()

    #global variables for constant values through out the recursion
    global algo
    global weights
    global depth
    #setting player variable here
    if str(ip[0]) == str("Star"):
        player = 1
    else:
        player = 0
    #setting algorithm variable here
    if ip[1] == 'MINIMAX':
        algo = 1
    else:
        algo = 0
    #setting depth of the tree
    depth = ip[2]
    #populating weights here
    weights = str(ip[11]).split(",")
    #create initial state of the board
    initial_state = [ str(i).split(",") for i in ip[3:11]]

    return player, initial_state

#main function to handle user interface
def main():
    player,initial_state = read_input_file()
    game_tree = Tree()
    game_tree.tree_creation(player, initial_state, parent)

#call to main function
if __name__ == '__main__':
    main()