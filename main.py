"""
@author Meghraj Bendre
@email bendre@usc.edu

Usage: python main.py
"""

import copy


#global variables for constant values through out the recursion
global algo
global weights
global depth

#simple class for node manipulation
class Node:
    def __init__(self, player, state, parent=None):
        self.player = player
        self.state = state
        self.parent = parent    #keeps track of the parent
        self.children = []      #keeps track of the children for traversal

    #create complete game tree
    def tree_creation(self, player, initial_state, parent):
        temp_node = Node(player, initial_state, parent)
        #self.children.append(temp_node)   

#############################################################################

#interface for building tree 
def tree_creation(player, initial_state, root):
    if not root:
        root = Node(player, initial_state, None)
        return root

#move generation based on current position
def move_generation(visited_nodes, depth_cntr, parent):

    print "********************************************************"
    for i in parent.state:
        print "\n"
        for j in i:
            print j,
    print "\nDepth: ",depth_cntr       
    print "********************************************************"

    if parent.player:  #STAR
        print "STAR"

        #logic for searching the STARS
        cnt1 = -1 #8
        cnt2 = -1

        for i in parent.state:
            cnt1 += 1 #-1
            cnt2 = -1
            for j in i:
                cnt2 += 1

                if (list(j)[0]) == 'S':
                    print cnt1,cnt2     #cnt1,cnt2 is location of star on the board
                    print parent.state[cnt1][cnt2],cnt1,cnt2

                    if cnt1 != 0:   #check if star is in last row or not

                        if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                            #print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                            if (list(parent.state[cnt1-1][cnt2-1])[0] == 'C'):
                                if ((parent.state[cnt1-2][cnt2-2] == '0') or (( cnt1-2 == 0) and (list(parent.state[cnt1-2][cnt2-2])[0] == 'S'))):
                                    #recursive call and move to this position
                                    print "pri3"
                                    temp_state = copy.deepcopy(parent.state)
                                    #check for super-imposing moves on the last node
                                    if (temp_state[cnt1-2][cnt2-2] != '0') and (cnt1-2 == 0):
                                        last_row_cond = int(list(temp_state[cnt1-2][cnt2-2])[1])
                                        last_row_cond += 1
                                        temp_state[cnt1-2][cnt2-2] = "S" + str(last_row_cond)
                                    else:
                                        temp_state[cnt1-2][cnt2-2] = 'S1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1-1][cnt2-1] = '0'
                                    temp_node = Node(0, temp_state, parent)
                                    parent.children.append(temp_node)   #Add children here
                            else:
                                #skip
                                print "pri33"

                        if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                            #print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                            if (list(parent.state[cnt1-1][cnt2+1])[0] == 'C'):
                                if ((parent.state[cnt1-2][cnt2+2] == '0') or (( cnt1-2 == 0) and (list(parent.state[cnt1-2][cnt2+2])[0] == 'S'))):
                                    #recursive call and move to this position
                                    print "pri4"
                                    temp_state = copy.deepcopy(parent.state)
                                    #check for super-imposing moves on the last node
                                    if (temp_state[cnt1-2][cnt2+2] != '0') and (cnt1-2 == 0):
                                        last_row_cond = int(list(temp_state[cnt1-2][cnt2+2])[1])
                                        last_row_cond += 1
                                        temp_state[cnt1-2][cnt2+2] = "S" + str(last_row_cond)
                                    else:
                                        temp_state[cnt1-2][cnt2+2] = 'S1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1-1][cnt2+1] = '0'
                                    temp_node = Node(0, temp_state, parent)
                                    parent.children.append(temp_node)   #Add children here
                            else:
                                #skip 
                                print "pri44"                        

                        if ((cnt1-1 >=0 and cnt1-1 <= 7) and (cnt2-1 >=0 and cnt2-1 <= 7)):
                            #print parent.state[cnt1-1][cnt2-1],cnt1-1,cnt2-1
                            if ((parent.state[cnt1-1][cnt2-1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2-1])[0] == 'S'))):
                                #recursive call and move to this position
                                print "pri1"
                                temp_state = copy.deepcopy(parent.state)
                                #check for super-imposing moves on the last node
                                if (temp_state[cnt1-1][cnt2-1] != '0'):
                                    last_row_cond = int(list(temp_state[cnt1-1][cnt2-1])[1])
                                    last_row_cond += 1
                                    temp_state[cnt1-1][cnt2-1] = "S" + str(last_row_cond)
                                else:
                                    temp_state[cnt1-1][cnt2-1] = 'S1' 
                                temp_state[cnt1][cnt2] = '0'
                                temp_node = Node(0, temp_state, parent)
                                parent.children.append(temp_node)   #Add children here
                            else:
                                #logic for S in last row
                                print "pri11"
                                
                        if ((cnt1-1 >=0 and cnt1-1 <= 7) and (cnt2+1 >=0 and cnt2+1 <= 7)):
                            #print parent.state[cnt1-1][cnt2+1],cnt1-1,cnt2+1 
                            if ((parent.state[cnt1-1][cnt2+1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2+1])[0] == 'S'))):
                                #recursive call and move to this position
                                print "pri2"
                                temp_state = copy.deepcopy(parent.state)
                                #check for super-imposing moves on the last node
                                if temp_state[cnt1-1][cnt2+1] != '0':
                                    last_row_cond = int(list(temp_state[cnt1-1][cnt2+1])[1])
                                    last_row_cond += 1
                                    temp_state[cnt1-1][cnt2+1] = "S" + str(last_row_cond)
                                else:
                                    temp_state[cnt1-1][cnt2+1] = 'S1'
                                temp_state[cnt1][cnt2] = '0'
                                temp_node = Node(0, temp_state, parent)
                                parent.children.append(temp_node)
                            else:
                                #skip
                                print "pri22"
                            
                    else:
                        print "LAST ROW BRO"

        depth_cntr -= 1
        if depth_cntr < 0:
            return
        for i in parent.children:
            visited_nodes += 1
            print "\nVisted Nodes: ",visited_nodes
            move_generation(visited_nodes, depth_cntr, i)

    else:
        print "CIRCLE"
        #logic for searching the STARS
        cnt1 = -1 #8
        cnt2 = -1

        for i in parent.state:
            cnt1 += 1 #-1
            cnt2 = -1
            for j in i:
                cnt2 += 1

                if (list(j)[0]) == 'C':
                    print cnt1,cnt2     #cnt1,cnt2 is location of star on the board
                    print parent.state[cnt1][cnt2],cnt1,cnt2

                    if cnt1 != 7:   #check if star is in last row or not

                        if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                            #print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                            print "pri31"
                            if (list(parent.state[cnt1+1][cnt2-1])[0] == 'S'):
                                print "pri32"
                                if ((parent.state[cnt1+2][cnt2-2] == '0') or (( cnt1+2 == 7) and (list(parent.state[cnt1+2][cnt2-2])[0] == 'C'))):
                                    #recursive call and move to this position
                                    print "pri33"
                                    temp_state = copy.deepcopy(parent.state)
                                    #check for super-imposing moves on the last node
                                    if (temp_state[cnt1+2][cnt2-2] != '0') and (cnt1+2 == 7):
                                        last_row_cond = int(list(temp_state[cnt1+2][cnt2-2])[1])
                                        last_row_cond += 1
                                        temp_state[cnt1+2][cnt2-2] = "C" + str(last_row_cond)
                                    else:
                                        temp_state[cnt1+2][cnt2-2] = 'C1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1+1][cnt2-1] = '0'
                                    temp_node = Node(0, temp_state, parent)
                                    parent.children.append(temp_node)   #Add children here
                            else:
                                #skip
                                print "pri33"

                        if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                            #print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                            if (list(parent.state[cnt1+1][cnt2+1])[0] == 'S'):
                                if ((parent.state[cnt1+2][cnt2+2] == '0') or (( cnt1+2 == 7) and (list(parent.state[cnt1+2][cnt2+2])[0] == 'C'))):
                                    #recursive call and move to this position
                                    print "pri4"
                                    temp_state = copy.deepcopy(parent.state)
                                    #check for super-imposing moves on the last node
                                    if (temp_state[cnt1+2][cnt2+2] != '0') and (cnt1+2 == 7):
                                        last_row_cond = int(list(temp_state[cnt1+2][cnt2+2])[1])
                                        last_row_cond += 1
                                        temp_state[cnt1+2][cnt2+2] = "C" + str(last_row_cond)
                                    else:
                                        temp_state[cnt1+2][cnt2+2] = 'C1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1+1][cnt2+1] = '0'
                                    temp_node = Node(0, temp_state, parent)
                                    parent.children.append(temp_node)   #Add children here
                            else:
                                #skip 
                                print "pri44"                                 


                        if ((cnt1+1 >=0 and cnt1+1 <= 7) and (cnt2-1 >=0 and cnt2-1 <= 7)):
                            print parent.state[cnt1+1][cnt2-1],cnt1+1,cnt2-1
                            if ((parent.state[cnt1+1][cnt2-1] == '0') or ((cnt1+1 == 7) and (list(parent.state[cnt1+1][cnt2-1])[0] == 'C'))):
                                #recursive call and move to this position
                                print "pri1"
                                temp_state = copy.deepcopy(parent.state)
                                #check for super-imposing moves on the last node
                                if (temp_state[cnt1+1][cnt2-1] != '0'):
                                    last_row_cond = int(list(temp_state[cnt1+1][cnt2-1])[1])
                                    last_row_cond += 1
                                    temp_state[cnt1+1][cnt2-1] = "C" + str(last_row_cond)
                                else:
                                    temp_state[cnt1+1][cnt2-1] = 'C1' 

                                temp_state[cnt1][cnt2] = '0'
                                temp_node = Node(1, temp_state, parent)
                                parent.children.append(temp_node)
                            else:
                                #skip
                                print "pri11"

                        if ((cnt1+1 >=0 and cnt1+1 <= 7) and (cnt2+1 >=0 and cnt2+1 <= 7)):
                            print parent.state[cnt1+1][cnt2+1],cnt1+1,cnt2+1 
                            if ((parent.state[cnt1+1][cnt2+1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2+1])[0] == 'C'))):
                                #recursive call and move to this position
                                print "pri2"
                                temp_state = copy.deepcopy(parent.state)
                                #check for super-imposing moves on the last node
                                if temp_state[cnt1+1][cnt2+1] != '0':
                                    last_row_cond = int(list(temp_state[cnt1+1][cnt2+1])[1])
                                    last_row_cond += 1
                                    temp_state[cnt1+1][cnt2+1] = "C" + str(last_row_cond)
                                else:
                                    temp_state[cnt1+1][cnt2+1] = 'C1'
                                temp_state[cnt1][cnt2] = '0'
                                temp_node = Node(0, temp_state, parent)
                                parent.children.append(temp_node)
                            else:
                                #skip
                                print "pri22"
                    else:
                        print "LAST ROW BRO"
                                    
        depth_cntr -= 1
        if depth_cntr < 0:
            return
        for i in parent.children:
            visited_nodes += 1
            print "\nVisted Nodes: ",visited_nodes
            move_generation(visited_nodes, depth_cntr, i)
                           
                     


###################################################################################################################
#reads input file and does necessary formatting
def read_input_file():
    input_file = open("input.txt")
    ip = input_file.read().splitlines()

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
    depth = int(ip[2])
    #populating weights here
    weights = str(ip[11]).split(",")
    #create initial state of the board
    initial_state = [ str(i).split(",") for i in ip[3:11]]

    return depth, player, initial_state

#main function to handle user interface
def main():
    depth_cntr, player, initial_state = read_input_file()
    root = None
    visited_nodes = 1
    root = tree_creation(player, initial_state, None) #created root here
    print "ROOT CREATED\n"
    #create tree here
    move_generation(visited_nodes, depth_cntr, root)    #testing traversal


#call to main function
if __name__ == '__main__':
    main()