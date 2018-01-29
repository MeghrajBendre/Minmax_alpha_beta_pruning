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
global pass_cntr_star
global pass_cntr_circle
global visited_nodes

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
def move_generation(depth_cntr, parent):

    print "********************************************************"
    for i in parent.state:
        print "\n"
        for j in i:
            print j,
    print "\nDepth: ",depth_cntr       
    print "********************************************************"
    global pass_cntr_star
    global pass_cntr_circle
    global visited_nodes

    if parent.player:  #STAR
        print "STAR"

        #logic for searching the STARS
        cnt1 = -1 #8
        cnt2 = -1
        breaker = 0
        for i in parent.state:
            cnt1 += 1 #-1
            cnt2 = -1
            pass_check_cntr_star = 0
            for j in i:
                cnt2 += 1
                print "Value in j: ",list(j)[0]
                if (list(j)[0]) == 'S':
                    #print cnt1,cnt2     #cnt1,cnt2 is location of star on the board
                    #print parent.state[cnt1][cnt2],cnt1,cnt2
                    print "Checking for each element"
                    if cnt1 != 0:   #check if star is in last row or not
                        print "NOT LAST ROW"
                        if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                            #print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                            if (list(parent.state[cnt1-1][cnt2-1])[0] == 'C'):
                                if ((parent.state[cnt1-2][cnt2-2] == '0') or (( cnt1-2 == 0) and (list(parent.state[cnt1-2][cnt2-2])[0] == 'S'))):
                                    #recursive call and move to this position
                                    print ""
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

                        if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                            #print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                            if (list(parent.state[cnt1-1][cnt2+1])[0] == 'C'):
                                if ((parent.state[cnt1-2][cnt2+2] == '0') or (( cnt1-2 == 0) and (list(parent.state[cnt1-2][cnt2+2])[0] == 'S'))):
                                    #recursive call and move to this position
                                    print ""
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

                        if ((cnt1-1 >=0 and cnt1-1 <= 7) and (cnt2-1 >=0 and cnt2-1 <= 7)):
                            #print parent.state[cnt1-1][cnt2-1],cnt1-1,cnt2-1
                            if ((parent.state[cnt1-1][cnt2-1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2-1])[0] == 'S'))):
                                #recursive call and move to this position
                                print ""
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
                                
                        if ((cnt1-1 >=0 and cnt1-1 <= 7) and (cnt2+1 >=0 and cnt2+1 <= 7)):
                            #print parent.state[cnt1-1][cnt2+1],cnt1-1,cnt2+1 
                            if ((parent.state[cnt1-1][cnt2+1] == '0') or ((cnt1-1 == 0) and (list(parent.state[cnt1-1][cnt2+1])[0] == 'S'))):
                                #recursive call and move to this position
                                print ""
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
                        print "LAST ROW"
                        pass_check_cntr_star = 4
                else:
                    print "Not a Star"
                print "Internal pass counter:",pass_check_cntr_star


                if pass_check_cntr_star == 4:   #pass check
                    pass_cntr_star += 1
                    print "PASS Inside: ",pass_cntr_star
                    if pass_cntr_star ==  2:
                        print "PASS Inside: Terminated"
                        depth_cntr = 0
                        breaker = 1
                        break
                    else:
                        parent.player = 0
                        move_generation(depth_cntr, parent)

            if breaker == 1:
                break

        if ((breaker == 0) and (len(parent.children == 0))):
            pass_cntr_star += 1
            print "PASS Outside: ",pass_cntr_star
            if pass_cntr_star ==  2:
                print "PASS Outside: Terminated"
                depth_cntr = 0
            else:
                parent.player = 0
                move_generation(depth_cntr, parent)

        depth_cntr -= 1
        #Check terminating conditions
        if depth_cntr < 0:  #depth check
            return

        #call children of the parent
        for i in parent.children:
            visited_nodes += 1
            print "\nVisted Nodes: ",visited_nodes
            move_generation(depth_cntr, i)

    else:
        print "CIRCLE"
        #logic for searching the STARS
        cnt1 = -1 #8
        cnt2 = -1
        breaker = 0

        for i in parent.state:
            cnt1 += 1 #-1
            cnt2 = -1
            pass_check_cntr_circle = 0
            for j in i:
                cnt2 += 1

                if (list(j)[0]) == 'C':
                    #print cnt1,cnt2     #cnt1,cnt2 is location of star on the board
                    #print parent.state[cnt1][cnt2],cnt1,cnt2

                    if cnt1 != 7:   #check if star is in last row or not                    

                        if ((cnt1+1 >=0 and cnt1+1 <= 7) and (cnt2-1 >=0 and cnt2-1 <= 7)):
                            print parent.state[cnt1+1][cnt2-1],cnt1+1,cnt2-1
                            if ((parent.state[cnt1+1][cnt2-1] == '0') or ((cnt1+1 == 7) and (list(parent.state[cnt1+1][cnt2-1])[0] == 'C'))):
                                #recursive call and move to this position
                                print ""
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
                                pass_check_cntr_circle += 1

                        if ((cnt1+1 >=0 and cnt1+1 <= 7) and (cnt2+1 >=0 and cnt2+1 <= 7)):
                            print "1"
                            #print parent.state[cnt1+1][cnt2+1],cnt1+1,cnt2+1 
                            if ((parent.state[cnt1+1][cnt2+1] == '0') or ((cnt1+1 == 7) and (list(parent.state[cnt1+1][cnt2+1])[0] == 'C'))):
                                #recursive call and move to this position
                                print "3"
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
                                #skip
                                pass_check_cntr_circle += 1


                        if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                            #print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                            print ""
                            if (list(parent.state[cnt1+1][cnt2-1])[0] == 'S'):
                                print ""
                                if ((parent.state[cnt1+2][cnt2-2] == '0') or (( cnt1+2 == 7) and (list(parent.state[cnt1+2][cnt2-2])[0] == 'C'))):
                                    #recursive call and move to this position
                                    print ""
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
                                #skip
                                pass_check_cntr_circle += 1

                        if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                            #print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                            if (list(parent.state[cnt1+1][cnt2+1])[0] == 'S'):
                                if ((parent.state[cnt1+2][cnt2+2] == '0') or (( cnt1+2 == 7) and (list(parent.state[cnt1+2][cnt2+2])[0] == 'C'))):
                                    #recursive call and move to this position
                                    print ""
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
                                #skip
                                pass_check_cntr_circle += 1                                

                    else:
                        print "LAST ROW BRO"
                        pass_check_cntr_circle = 4
                else:
                    print "Not a Star"
                print "Internal pass counter:",pass_check_cntr_circle


                if pass_check_cntr_circle == 4:   #pass check
                    pass_cntr_star += 1
                    print "PASS Inside: ",pass_cntr_star
                    if pass_cntr_star ==  2:
                        print "PASS Inside: Terminated"
                        depth_cntr = 0
                        breaker = 1
                        break
                    else:
                        parent.player = 1
                        move_generation(depth_cntr, parent)

            if breaker == 1:
                break
            
        if ((breaker == 0) and (len(parent.children == 0))):
            pass_cntr_star += 1
            print "PASS Outside: ",pass_cntr_star
            if pass_cntr_star ==  2:
                print "PASS Outside: Terminated"
                depth_cntr = 0
            else:
                parent.player = 1
                move_generation(depth_cntr, parent)

        depth_cntr -= 1
        #Check terminating conditions
        if depth_cntr < 0:  #depth check
            return

        for i in parent.children:
            visited_nodes += 1
            print "\nVisted Nodes: ",visited_nodes
            move_generation(depth_cntr, i)
                           
                     


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
    global pass_cntr_star
    global pass_cntr_circle
    visited_nodes = 1
    pass_cntr_star = 0
    pass_cntr_circlr = 0
    root = tree_creation(player, initial_state, None) #created root here
    print "ROOT CREATED\n"
    #create tree here
    move_generation(depth_cntr, root)    #testing traversal


#call to main function
if __name__ == '__main__':
    main()