from __future__ import division
from __future__ import print_function
from resource import getrusage, RUSAGE_SELF

from enum import Enum
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
            #print("Unable to move up when blank tile in first row.")
            return
        else:
            new_blank_tile_index = blank_tile_index - 3
            new_config[blank_tile_index], new_config[new_blank_tile_index] = new_config[new_blank_tile_index], new_config[blank_tile_index]
            return PuzzleState(new_config, self.n, self, "Up", self.cost+1) # consider the cost later once implement that function
      
    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        blank_tile_index = 0
        try:
            blank_tile_index = self.config.index(0)
        except ValueError as error:
            print(f"Bad puzzle configuration. Unable to find blank tile: {error}")
            return
        
        new_config = self.config.copy()
        if blank_tile_index > 5:
            #print("Unable to move down when blank tile in last row.")
            return
        else:
            new_blank_tile_index = blank_tile_index + 3
            new_config[blank_tile_index], new_config[new_blank_tile_index] = new_config[new_blank_tile_index], new_config[blank_tile_index]
            return PuzzleState(new_config, self.n, self, "Down", self.cost+1) # consider the cost later once implement that function
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        blank_tile_index = 0
        try:
            blank_tile_index = self.config.index(0)
        except ValueError as error:
            print(f"Bad puzzle configuration. Unable to find blank tile: {error}")
            return
        
        new_config = self.config.copy()
        if blank_tile_index % 3 == 0:
            #print("Unable to move left when blank tile in leftmost row.")
            return
        else:
            new_blank_tile_index = blank_tile_index - 1
            new_config[blank_tile_index], new_config[new_blank_tile_index] = new_config[new_blank_tile_index], new_config[blank_tile_index]
            return PuzzleState(new_config, self.n, self, "Left", self.cost+1) # consider the cost later once implement that function

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        blank_tile_index = 0
        try:
            blank_tile_index = self.config.index(0)
        except ValueError as error:
            print(f"Bad puzzle configuration. Unable to find blank tile: {error}")
            return
        
        new_config = self.config.copy()
        if blank_tile_index % 3 == 2:
            #print("Unable to move right when blank tile in rightmost row.")
            return
        else:
            new_blank_tile_index = blank_tile_index + 1
            new_config[blank_tile_index], new_config[new_blank_tile_index] = new_config[new_blank_tile_index], new_config[blank_tile_index]
            return PuzzleState(new_config, self.n, self, "Right", self.cost+1) # consider the cost later once implement that function
      
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
def writeOutput(path_to_goal, cost_of_path, nodes_expanded, search_depth, 
                max_search_depth, running_time, max_ram_usage):
    file = open("output.txt", "a")
    result_string = f'''path_to_goal: {path_to_goal}\n cost_of_path: {cost_of_path}\n
                   nodes_expanded: {nodes_expanded}\n search_depth: {search_depth}\n
                   max_search_depth: {max_search_depth}\n running_time: {running_time}\n
                   max_ram_usage: {max_ram_usage}'''
    file.write(result_string)
    print(result_string)
    file.close()
    
def bfs_search(initial_state):
    frontier = Q.Queue()
    frontier.put(initial_state)
    
    explored = set()
    nodes_expanded, max_search_depth = 0, 0
    while not frontier.empty():
        state = frontier.get()
        state_config = tuple(state.config)
        #print(state_config)
        explored.add(state_config)
        #print(explored)
        
        if test_goal(state):
            path_to_goal, search_depth = calculate_path_to_goal_and_search_depth(state)
            return {'path': path_to_goal, 'path_cost': state.cost, 'nodes_expanded':
                    nodes_expanded, 'depth': search_depth, 'max_depth': max_search_depth}
        children = state.expand()
        nodes_expanded += 1 # this is the right place to put this, right? Unit test/sanity check
        for child in children:
            child_config = tuple(child.config)
            if child_config not in explored:
                frontier.put(child)
        max_search_depth += 1 #make sure can test all of these in unit tests- or at least manually if too complicated
    return None
            

def dfs_search(initial_state):
    return uninformed_search(UninformedSearch.DFS, initial_state)

class UninformedSearch(Enum):
    BFS = 1
    DFS = 2

def uninformed_search(search_type, initial_state):
    frontier = Q.Queue() if search_type == UninformedSearch.BFS else Q.LifoQueue()
    frontier.put(initial_state)
    
    explored = set()
    nodes_expanded, max_search_depth = 0, 0
    while not frontier.empty():
        state = frontier.get()
        state_config = tuple(state.config)
        explored.add(state_config)
        
        if test_goal(state):
            #nuke search depth calculation because it's the same as the cost
            path_to_goal, search_depth = calculate_path_to_goal_and_search_depth(state)
            return {'path': path_to_goal, 'path_cost': state.cost, 'nodes_expanded':
                    nodes_expanded, 'depth': search_depth, 'max_depth': max_search_depth}
        children = state.expand()
        nodes_expanded += 1 # this is the right place to put this, right? Unit test/sanity check
        for child in children:
            child_config = tuple(child.config)
            if child_config not in explored:
                frontier.put(child)
        max_search_depth = max(max_search_depth, state.cost) # the cost is the same as the search depth
    return None
        

def A_star_search(initial_state):
    frontier = Q.PriorityQueue()
    """
    According to the Python doc priority queue implementation, items with the same priority in a Tuple break comparison.
    Resolve this via the recommended solution which is to store an entry "count" item. Fall back to this to break priority
    ties.
    """
    count = 0
    frontier.put((0, count, initial_state))
    explored = set()
    nodes_expanded, max_search_depth = 0, 0
    while not frontier.empty():
        state_info = frontier.get()
        state = state_info[2]
        explored.add(tuple(state.config))

        if test_goal(state):
            path_to_goal, search_depth = calculate_path_to_goal_and_search_depth(state)
            return {'path': path_to_goal, 'path_cost': state.cost, 'nodes_expanded':
                    nodes_expanded, 'depth': search_depth, 'max_depth': max_search_depth}
        children = state.expand()
        nodes_expanded += 1 # this is the right place to put this, right? Unit test/sanity check
        for child in children:
            child_config = tuple(child.config)
            if child_config not in explored:
                # duplicates will be distinguished by estimated cost
                # we ignore duplicates once we explored our designated
                # min cost representation.
                estimated_total_cost = calculate_total_cost(child)
                count += 1
                frontier.put((estimated_total_cost, count, child))
        max_search_depth += 1 #make sure can test all of these in unit tests- or at least manually if too complicated
    return None

def calculate_total_cost(state):
    total_manhattan_dist = 0
    for index, value in enumerate(state.config):
        tile_dist = calculate_manhattan_dist(index, value, None)
        total_manhattan_dist += tile_dist
    return state.cost + total_manhattan_dist

def calculate_manhattan_dist(idx, value, n): # n isn't used in my implementation, but keeping it to avoid breaking autograder
    true_locs = {0: (0, 0), 1: (0, 1), 2: (0, 2), 
                      3: (1, 0), 4: (1, 1), 5: (1, 2),
                      6: (2, 0), 7: (2, 1), 8: (2, 2)}

    # calculate horizontal distance
    true_col = true_locs[value][1]
    curr_col = idx % 3
    horizontal_dist = abs(true_col-curr_col)
    
    # calculate vertical distance
    true_row = true_locs[value][0]
    curr_row = 0
    if 2 < idx < 6: curr_row = 1
    if 5 < idx: curr_row = 2
    vertical_dist = abs(true_row-curr_row)
    
    return horizontal_dist+vertical_dist

def test_goal(puzzle_state) -> bool:
    return puzzle_state.config == [0,1,2,3,4,5,6,7,8]


def calculate_path_to_goal_and_search_depth(state):
    curr_state = state
    path, search_depth = [], 0
    while curr_state.parent:
        search_depth += 1
        path.append(curr_state.action)
        curr_state = curr_state.parent
    path.reverse()
    return path, search_depth
        
def write_result_info(result_info, start_time):
    if not result_info: return #figure out how to handle empty case- should just be the empty config? No solution vs. handed goal state?
    end_time = time.time()
    max_RAM = getrusage(RUSAGE_SELF).ru_maxrss
    writeOutput(result_info['path'], result_info['path_cost'], result_info['nodes_expanded'],result_info['depth'], result_info['max_depth'], end_time-start_time, max_RAM)

    # Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if search_mode == "bfs":
        result_info = bfs_search(hard_state)
        write_result_info(result_info, start_time)
    elif search_mode == "dfs":
        result_info = dfs_search(hard_state)
        write_result_info(result_info, start_time)
    elif search_mode == "ast": 
        result_info = A_star_search(hard_state)
        write_result_info(result_info, start_time)
    else: 
        print("Enter valid command arguments !")

if __name__ == '__main__':
    main()
