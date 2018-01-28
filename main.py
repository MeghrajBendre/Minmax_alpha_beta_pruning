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

    def children_addition(self, temp_node):
        self.children_addition(temp_node)

    #create complete game tree
    def tree_creation(self, player, initial_state, parent):
        temp_node = Node(player, initial_state, parent)
        self.children_addition(temp_node)   


#class to construct the game tree 
class Tree:
    def __init__(self):
        self.root = None

    #interface for building tree 
    def tree_creation(self, player, initial_state, parent):
        if self.root:
            return self.root.tree_creation(player, initial_state, parent)  ######FIGURE OUT HOW TO CALL THIS AFTER ROOT IS CREATED
        else:
            self.root = Node(player, initial_state, parent)

    #move generation based on current position
    def move_generation(self, player, state, parent):
        if player:  #STAR
            print "STAR"

            temp_node = Node(player, state, parent)

            #logic for searching the STARS
            cnt1 = 8
            cnt2 = -1
            for i in state:
                cnt1 -= 1
                cnt2 = -1
                for j in i:
                    cnt2 += 1
                    if (list(j)[0]) == 'S':
                        #print cnt1,cnt2     #cnt1,cnt2 is location of star on the board
        else:
            print "CIRCLE"
            cnt1 = 8
            cnt2 = -1
            for i in state:
                cnt1 -= 1
                cnt2 = -1
                for j in i:
                    cnt2 += 1
                    if (list(j)[0]) == 'C':
                        #print cnt1,cnt2     #cnt1,cnt2 is location of circle on the board
                     



###################################################################################################################
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
    #game_tree.tree_creation(player, initial_state, parent=None) #created root here
    #create tree here
    game_tree.move_generation(player, initial_state, parent=None)    #testing traversal
   

#call to main function
if __name__ == '__main__':
    main()