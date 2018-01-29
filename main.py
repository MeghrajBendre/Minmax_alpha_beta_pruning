"""
@author Meghraj Bendre
@email bendre@usc.edu

Usage: python main.py
"""

import copy


#global variables for constant values through out the recursion
global algo
global weight
global depth
global pass_cntr
global visited_nodes

#simple class for node manipulation
class Node:
    def __init__(self, player, state, parent=None, value=0, name='', pas=0):
        self.value = value      #for storing min max value
        self.name = name        #PATH
        self.pas = pas          #pass counter for each state
        self.player = player
        self.state = state
        self.parent = parent    #keeps track of the parent
        self.children = []      #keeps track of the children for traversal  
#############################################################################

#interface for root creation 
def tree_creation(player, initial_state, root):
    if not root:
        root = Node(player, initial_state, None)
        return root

def is_game_over(board):
    has_star = False
    has_circle = False
    for i in board:
        for j in i:
            if list(j)[0] == 'S':
                has_star = True
            elif list(j)[0] == 'C':
                has_circle = True
    return not(has_star and has_circle) 

#move generation based on current position
def move_generation(depth_cntr, parent):
    #printing each new iteration here
    print "********************************************************"
    for i in parent.state:
        print "\n"
        for j in i:
            print j,
    print "\nDepth: ",depth_cntr
    print "\nPlayer: ",parent.player
    print "\nNo of children: ",len(parent.children)      
    print "********************************************************"

    global pass_cntr
    global visited_nodes

    #Check terminating conditions
    if depth_cntr == 0 or is_game_over(parent.state):  #depth check
        return

    if parent.player:  #STAR i.e. player is 1
        print "STAR"
        #logic for searching the STARS
        cnt1 = -1 #8
        cnt2 = -1
        #breaker = 0
        for i in parent.state:
            cnt1 += 1 #-1
            cnt2 = -1
            pass_check_cntr_star = 0
            for j in i:
                cnt2 += 1
                #print "Value in j: ",list(j)[0]
                if (list(j)[0]) == 'S':
                    print parent.state[cnt1][cnt2],cnt1,cnt2

                    #THESE ARE BASICALLY VALID MOVES 1.keep counter of S here 2.keep count of skipped moves
                    if cnt1 != 0:   #check if star is in last row or not

                        if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                            #print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                            if (list(parent.state[cnt1-1][cnt2-1])[0] == 'C'):
                                if ((parent.state[cnt1-2][cnt2-2] == '0') or (( cnt1-2 == 0) and (list(parent.state[cnt1-2][cnt2-2])[0] == 'S'))):
                                    #recursive call and move to this position
                                    
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
                                print "pri1"
                                pass_check_cntr_star += 1
                        else:
                            #skip
                            print "pri11"
                            pass_check_cntr_star += 1

                        if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                            #print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                            if (list(parent.state[cnt1-1][cnt2+1])[0] == 'C'):
                                if ((parent.state[cnt1-2][cnt2+2] == '0') or (( cnt1-2 == 0) and (list(parent.state[cnt1-2][cnt2+2])[0] == 'S'))):
                                    #recursive call and move to this position
                                    
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
                                print "pri2"
                                pass_check_cntr_star += 1
                        else:
                            #skip
                            print "pri22"
                            pass_check_cntr_star += 1                     

                        if ((cnt1-1 >=0 and cnt1-1 <= 7) and (cnt2-1 >=0 and cnt2-1 <= 7)):
                            #print parent.state[cnt1-1][cnt2-1],cnt1-1,cnt2-1
                            if ((parent.state[cnt1-1][cnt2-1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2-1])[0] == 'S'))):
                                #recursive call and move to this position
                                
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
                                #Skip
                                print "pri3"
                                pass_check_cntr_star += 1
                        else:
                            #Skip
                            print "pri33"
                            pass_check_cntr_star += 1
                            
                        if ((cnt1-1 >=0 and cnt1-1 <= 7) and (cnt2+1 >=0 and cnt2+1 <= 7)):
                            #print parent.state[cnt1-1][cnt2+1],cnt1-1,cnt2+1 
                            if ((parent.state[cnt1-1][cnt2+1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2+1])[0] == 'S'))):
                                #recursive call and move to this position
                                
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
                                #Skip
                                print "pri4"
                                pass_check_cntr_star += 1
                        else:
                            #Skip
                            print "pri44"
                            pass_check_cntr_star += 1
                
                        if pass_check_cntr_star == 4: #no move for a state and should be a pass
                            print "No valid move for this piece of S"
                    else:
                        print "Last Row"        
               # else:
                    #print "Empty location"
                    #print "Not a Star"

               # print "Pass Counter ",pass_check_cntr_star

        #IF counter_of_S ==  pass_check_cntr_star/4 ---> PASS      

        #if no children for current node, pass
        print "No of children before checks: ",len(parent.children)
        if len(parent.children) == 0:
            parent.pas += 1
            print "PASS from STAR: ",parent.pas
            if parent.pas == 2:
                print "PASS: TERMINATION"
                depth = 0
            else:
                parent.player = 0   #call Circle now
                visited_nodes += 1
                print "\nVisted Nodes: ",visited_nodes
                move_generation(depth_cntr-1, parent)
        else:
        #call children of the parent
            for i in parent.children:
                visited_nodes += 1
                print "\nVisted Nodes: ",visited_nodes
                move_generation(depth_cntr-1, i)

        #Check terminating conditions
        #if depth_cntr < 0:  #depth check
        #    return



    else:
        print "CIRCLE"
        #logic for searching the STARS
        cnt1 = -1 #8
        cnt2 = -1
        #breaker = 0
        for i in parent.state:
            cnt1 += 1 #-1
            cnt2 = -1
            pass_check_cntr_circle = 0
            for j in i:
                cnt2 += 1

                if (list(j)[0]) == 'C':
                    #print cnt1,cnt2     #cnt1,cnt2 is location of star on the board
                    print parent.state[cnt1][cnt2],cnt1,cnt2                   
                    if (cnt1 != 7):
                        if ((cnt1+1 >=0 and cnt1+1 <= 7) and (cnt2-1 >=0 and cnt2-1 <= 7)):
                            print parent.state[cnt1+1][cnt2-1],cnt1+1,cnt2-1
                            if ((parent.state[cnt1+1][cnt2-1] == '0') or ((cnt1+1 == 7) and (list(parent.state[cnt1+1][cnt2-1])[0] == 'C'))):
                                #recursive call and move to this position
                                
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
                                #Skip
                                print "pri1"
                                pass_check_cntr_circle += 1
                        else:
                            #Skip
                            print "pri11"
                            pass_check_cntr_circle += 1

                        if ((cnt1+1 >=0 and cnt1+1 <= 7) and (cnt2+1 >=0 and cnt2+1 <= 7)):
                            #print parent.state[cnt1+1][cnt2+1],cnt1+1,cnt2+1 
                            if ((parent.state[cnt1+1][cnt2+1] == '0') or ((cnt1+1 == 7) and (list(parent.state[cnt1+1][cnt2+1])[0] == 'C'))):
                                #recursive call and move to this position
                                
                                temp_state = copy.deepcopy(parent.state)
                                #check for super-imposing moves on the last node
                                if temp_state[cnt1+1][cnt2+1] != '0':
                                    last_row_cond = int(list(temp_state[cnt1+1][cnt2+1])[1])
                                    last_row_cond += 1
                                    temp_state[cnt1+1][cnt2+1] = "C" + str(last_row_cond)
                                else:
                                    temp_state[cnt1+1][cnt2+1] = 'C1'
                                temp_state[cnt1][cnt2] = '0'
                                temp_node = Node(1, temp_state, parent)
                                parent.children.append(temp_node)
                            else:
                                #Skip
                                print "pri2"
                                pass_check_cntr_circle += 1
                        else:
                            #Skip
                            print "pri22"
                            pass_check_cntr_circle += 1

                        if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                            #print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                            
                            if (list(parent.state[cnt1+1][cnt2-1])[0] == 'S'):
                                
                                if ((parent.state[cnt1+2][cnt2-2] == '0') or (( cnt1+2 == 7) and (list(parent.state[cnt1+2][cnt2-2])[0] == 'C'))):
                                    #recursive call and move to this position
                                    
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
                                    temp_node = Node(1, temp_state, parent)
                                    parent.children.append(temp_node)   #Add children here
                            else:
                                #Skip
                                print "pri3"
                                pass_check_cntr_circle += 1
                        else:
                            #Skip
                            print "pri33"
                            pass_check_cntr_circle += 1

                        if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                            #print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                            if (list(parent.state[cnt1+1][cnt2+1])[0] == 'S'):
                                if ((parent.state[cnt1+2][cnt2+2] == '0') or (( cnt1+2 == 7) and (list(parent.state[cnt1+2][cnt2+2])[0] == 'C'))):
                                    #recursive call and move to this position
                                    
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
                                    temp_node = Node(1, temp_state, parent)
                                    parent.children.append(temp_node)   #Add children here
                            else:
                                #Skip
                                print "pri4"
                                pass_check_cntr_circle += 1 
                        else:
                            #Skip
                            print "pri44"
                            pass_check_cntr_circle += 1                            
                        
                        if pass_check_cntr_circle == 4: #no move for a state and should be a pass
                            print "No valid move for this piece of S"
                    else:
                        print "Last Row" 
                
                    #print "Not a Circle"
                #print "Internal pass counter:",pass_check_cntr_circle

        #if no children for current node, pass
        print "No of children before checks: ",len(parent.children)
        if len(parent.children) == 0:
            parent.pas += 1
            print "PASS from CIRCLE: ",parent.pas
            if parent.pas == 2:
                print "PASS: TERMINATION"
                depth = 0
            else:
                parent.player = 1   #call Circle now
                visited_nodes += 1
                print "\nVisted Nodes: ",visited_nodes
                move_generation(depth_cntr-1, parent)
        else:
        #call children of the parent
            for i in parent.children:
                visited_nodes += 1
                print "\nVisted Nodes: ",visited_nodes
                move_generation(depth_cntr-1, i)

        #Check terminating conditions
        #if depth_cntr < 0:  #depth check
        #    return
                           
    return  #final return of moves_generation             


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
    
    global visited_nodes
    global pass_cntr
    
    visited_nodes = 1
    pass_cntr = 0
    pass_cntr_circlr = 0
    root = tree_creation(player, initial_state, None) #created root here
    print "ROOT CREATED\n"
    #create tree here
    print "\nVisted Nodes: ",visited_nodes
    move_generation(depth_cntr, root)    #testing traversal


#call to main function
if __name__ == '__main__':
    main()