"""
@author Meghraj Bendre
@email bendre@usc.edu

Usage: python main.py
"""

import copy


#global variables for constant values through out the recursion
global MAX
global weights
global depth
global pass_cntr
global visited_nodes
global algo




#simple class for node manipulation
class Node:
    def __init__(self, player, state, parent=None, name="", value=0, pas=0):
        self.name = name
        self.value = value      #for storing min max value
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
        root.name = "ROOT"
        return root

#utility function
def utility_eval(board): #current_node.player
    a = -1
    sum_star = int(0)
    sum_circle = int(0)
    global weights
    for i in board:
        a += 1
        for j in i:
            if list(j)[0] == 'S':
                print "star1: ",int(list(j)[1])
                print "star2: ",int(weights[(a*(-1))-1])
                sum_star += (int(list(j)[1]) * int(weights[(a*(-1))-1]))
            if list(j)[0] == 'C':
                print "circle1: ",int(list(j)[1])
                print "circle2: ",int(weights[a])
                sum_circle += (int(list(j)[1]) * int(weights[a]))
    
    print "sum of stars: ",sum_star
    print "sum of circle: ",sum_circle

    if MAX:  #STAR and MAX
        print "RETURN: 1st :: ",int(sum_star - sum_circle)
        return int(sum_star - sum_circle)
    else:       #CIRCLE and MAX
        print "RETURN: 2nd ::",int(sum_circle-sum_star)
        return int(sum_circle - sum_star)



#check if 1.No pieces on board 2.Only Stars 3.Only circles 
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
def move_generation(alpha, beta, depth_cntr, parent):
    #printing each new iteration here
    print "********************************************************"
    print "\nNode Name: ",parent.name
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
    global algo
    
    
    move = ""

    #Check terminating conditions
    if depth_cntr == 0 or is_game_over(parent.state):  #depth check
        print "Move1: " + str(move)
        return move, int(utility_eval(parent.state))

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
                                    print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+2)) + str(cnt2+1-2)
                                    temp_node = Node(0, temp_state, parent)
                                    temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+2)) + str(cnt2+1-2))
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
                                    print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+1)) + str(cnt2+1+1)
                                    temp_node = Node(0, temp_state, parent)
                                    temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+2)) + str(cnt2+2+1))
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
                                print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+1)) + str(cnt2+1-1)
                                temp_node = Node(0, temp_state, parent)
                                temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+1)) + str(cnt2+1-1))
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
                                print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+1)) + str(cnt2+1+1)                       
                                temp_node = Node(0, temp_state, parent)
                                temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1+1)) + str(cnt2+1+1))
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
        
        #If STAR is MAX
        if MAX == 1:
            infinity = float('inf')
            max_value = -infinity
        else:
            infinity = float('inf')
            min_value = infinity

        print "No of children before checks: ",len(parent.children)
        if len(parent.children) == 0:
            if parent.pas == 2:
                move = "pass"
                print "Move2: " + str(move)
                return move, utility_eval(parent.state)
            else:
                temp_node = Node(0, copy.deepcopy(parent.state), parent)
                temp_node.name = "pass"
                temp_node.pas = parent.pas + 1
                parent.children.append(temp_node)
                
                            
        #call children of the parent
        for i in parent.children:
            visited_nodes += 1
            print "\nVisted Nodes: ",visited_nodes
            m, x = move_generation(alpha, beta, depth_cntr-1, i)
            i.value = x
            if MAX == 1:
                if x > max_value:
                    max_value = x
                    move = str(i.name)
                    print "Move33: " + str(move)
                    alpha = max(alpha, max_value)
                    if algo and alpha >= beta:
                        return move, max_value
            else:
                if x < min_value:
                    min_value = x
                    move = str(i.name)
                    print "Move44: " + str(move)
                    beta = min(beta, min_value)
                    if algo and alpha >= beta:
                        return move, min_value
        if MAX == 1:
            print "Move3: " + str(move)
            return move, max_value
        else:
            print "Move4: " + str(move)
            return move, min_value 


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
                                print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-1)) + str(cnt2+1-1)
                                temp_node = Node(1, temp_state, parent)
                                temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-1)) + str(cnt2+1-1))
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
                                print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-1)) + str(cnt2+1+1)
                                temp_node = Node(1, temp_state, parent)
                                temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-1)) + str(cnt2+1+1))
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
                                    print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-2)) + str(cnt2+1-2)
                                    temp_node = Node(1, temp_state, parent)
                                    temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-2)) + str(cnt2+1-2))
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
                                    print "lol" + str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-2)) + str(cnt2+1+2)
                                    temp_node = Node(1, temp_state, parent)
                                    temp_node.name = str(str(chr(72-cnt1)) + str(cnt2+1) + "-" + str(chr(72-cnt1-2)) + str(cnt2+1+2))
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

                #If STAR is MAX
        if MAX == 0:
            infinity = float('inf')
            max_value = -infinity
        else:
            infinity = float('inf')
            min_value = infinity

        print "No of children before checks: ",len(parent.children)
        if len(parent.children) == 0:
            if parent.pas == 2:
                move = "pass"
                print "Move5: " + str(move)
                return move, utility_eval(parent.state)
            else:
                temp_node = Node(1, copy.deepcopy(parent.state), parent)
                temp_node.name = "pass"
                temp_node.pas = parent.pas + 1
                parent.children.append(temp_node)


        #call children of the parent
        for i in parent.children:
            visited_nodes += 1
            print "\nVisted Nodes: ",visited_nodes
            m, x = move_generation(alpha, beta, depth_cntr-1, i)
            i.value = x
            if MAX == 0:
                if x > max_value:
                    max_value = x
                    move = str(i.name)
                    print "Move66:" + move
                    alpha = max(alpha, max_value)
                    if algo and alpha >= beta:
                        return move, max_value
            else:
                if x < min_value:
                    min_value = x
                    move = str(i.name)
                    print "Move77:" + move
                    beta = min(beta, min_value)
                    if algo and alpha >= beta:
                        return move, min_value
        if MAX == 0:
            print "Move6: " + move
            return move, max_value
        else:
            print "Move7: " + move
            return move, min_value 

###################################################################################################################
#reads input file and does necessary formatting
def read_input_file():
    input_file = open("input.txt")
    ip = input_file.read().splitlines()
    input_file.close()

    global MAX
    global weights
    global algo

    #setting player variable here
    if str(ip[0]) == str("Star"):
        MAX = 1
    else:
        MAX = 0
    #setting algorithm variable here
    if ip[1] == 'MINIMAX':
        algo = 0
    else:
        algo = 1
    #setting depth of the tree
    depth = int(ip[2])
    #populating weights here
    weights = str(ip[11]).split(",")
    #create initial state of the board
    initial_state = [ str(i).split(",") for i in ip[3:11]]

    return depth, initial_state

#main function to handle user interface
def main():
    depth_cntr, initial_state = read_input_file()
    root = None
    
    global visited_nodes
    global pass_cntr
    global MAX
    
    

    infinity = float('inf')
    alpha = -infinity
    beta = infinity

    visited_nodes = 1
    pass_cntr = 0
    pass_cntr_circlr = 0
    move = ""
    root = tree_creation(MAX, initial_state, None) #created root here
    print "ROOT CREATED\n"
    #create tree here
    print "\nVisted Nodes: ",visited_nodes
    move, best_move = move_generation(alpha, beta, depth_cntr, root)    #testing traversal

    #calculating myopic utility
    if root:
        print len(root.children)
        for child in root.children:
            if child.name == move:
                    for i in child.state:
                        print "\n"
                        for j in i:
                            print j,
                    lol = utility_eval(child.state)
                    print "LOLOL: " + str(lol)
                

    #writing to the output file
    op = open("output.txt","w")
    op.write(str(move) + "\n")
    op.write(str(lol) + "\n")
    op.write(str(best_move) + "\n")    
    op.write(str(visited_nodes) + "\n")

    op.close()


#call to main function
if __name__ == '__main__':
    main()