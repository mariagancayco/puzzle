from __future__ import division
from __future__ import print_function

import sys
import math
import time
import queue as Q


#### SKELETON CODE ####
## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])

    def move_up(self):
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        blank_tile_index = 0
        try:
            blank_tile_index = self.config.index(0)
        except ValueError as error:
            print(f"Bad puzzle configuration. Unable to find blank tile: {error}")
            return
        
        new_config = self.config.copy()
        if blank_tile_index < 3:
            print("Unable to move up when blank tile in first row.")
            return
        else:
            new_blank_tile_index = blank_tile_index - 3
            new_config[blank_tile_index], new_config[new_blank_tile_index] = new_config[new_blank_tile_index], new_config[blank_tile_index]
            return PuzzleState(new_config, self.n, self, "Move Up") # consider the cost later once implement that function
      
    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        pass
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        pass

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        pass
      
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput():
    ### Student Code Goes here
    pass

def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    pass

def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    pass

def A_star_search(initial_state):
    frontier = Q.PriorityQueue((0, initial_state))
    explored = set()
    while not frontier.empty():
        cost, state = frontier.get()
        explored.add(state)
        if self.test_goal(state):
            return True
        for neighbor in state.neighbors:
            if neighbor not in explored and neighbor not in frontier:
                # duplicates will be distinguished by cost
                # we ignore duplicates once we explored our designated
                # min cost representation.
                frontier.put((calculate_total_cost(neighbor), neighbor))
    return False
        

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    pass

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    pass

def test_goal(puzzle_state) -> bool:
    return puzzle_state == [0,1,2,3,4,5,6,7,8]

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if   search_mode == "bfs": bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()
