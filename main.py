"""
@author Meghraj Bendre
@email bendre@usc.edu

Usage: python main.py
"""

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

#call to main function
if __name__ == '__main__':
    main()