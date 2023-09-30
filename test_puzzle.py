from puzzle import PuzzleState, calculate_manhattan_dist, bfs_search, dfs_search, A_star_search
import unittest

class TestPuzzleMethods(unittest.TestCase):
#    maxDiff = None
     
    def test_bfs_search_large_size_search(self):
        expected_result = {'path': ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], 'path_cost': 26, 'nodes_expanded':
                    166786, 'depth': 26, 'max_depth': 27}
        result = bfs_search(PuzzleState([8,6,4,2,1,3,5,7,0], 3))
        self.assert_search_results(expected_result, result)
        
    def test_dfs_search_large_size_search(self):
        expected_result = {'path': None, 'path_cost': 46142, 'nodes_expanded': 51015, 'depth': 46142, 'max_depth': 46142}
        result = dfs_search(PuzzleState([6,1,8,4,0,2,7,3,5], 3))
        self.assert_search_results(expected_result, result, False)
        
    def test_ast_search_medium_size_search(self):
        expected_result = {'path': ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], 'path_cost': 26, 'nodes_expanded': 1585, 'depth': 26, 'max_depth': 26}
        result = A_star_search(PuzzleState([8,6,4,2,1,3,5,7,0], 3))
        self.assert_search_results(expected_result, result)
        
    def test_bfs_search_medium_size_search(self):
        expected_result = {'path': ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], 'path_cost': 20, 'nodes_expanded':
                    54094, 'depth': 20, 'max_depth': 21}
        result = bfs_search(PuzzleState([6,1,8,4,0,2,7,3,5], 3))
        self.assert_search_results(expected_result, result)
        
    def test_dfs_search_medium_size_search(self):
        expected_result = {'path': None, 'path_cost': 9612, 'nodes_expanded': 9869, 'depth': 9612, 'max_depth': 9612}
        result = dfs_search(PuzzleState([8,6,4,2,1,3,5,7,0], 3))
        self.assert_search_results(expected_result, result, False)
        
    def test_ast_search_small_size_search(self):
        expected_result = {'path': ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], 'path_cost': 20, 'nodes_expanded': 696, 'depth': 20, 'max_depth': 20}
        result = A_star_search(PuzzleState([6,1,8,4,0,2,7,3,5], 3))
        self.assert_search_results(expected_result, result)
        
    def test_bfs_search_small_size_search(self):
        expected_result = {'path': ['Up', 'Left', 'Left'], 'path_cost': 3, 'nodes_expanded': 10, 'depth': 3, 'max_depth': 4}
        result = bfs_search(PuzzleState([1,2,5,3,4,0,6,7,8], 3))
        self.assert_search_results(expected_result, result)

    def test_dfs_search_small_size_search(self):
        expected_result = {'path': ['Up', 'Left', 'Left'], 'path_cost': 3, 'nodes_expanded': 181437, 'depth': 3, 'max_depth': 66125}
        result = dfs_search(PuzzleState([1,2,5,3,4,0,6,7,8], 3))
        self.assert_search_results(expected_result, result)

    def assert_search_results(self, expected_result, result, check_path=True):
        #if check_path:
        #    self.assertEqual(expected_result['path'], result['path'])
        #self.assertEqual(expected_result['path_cost'], result['path_cost'])
        # nodes_expanded is wrong for AST
        self.assertEqual(expected_result['nodes_expanded'], result['nodes_expanded'])
        #self.assertEqual(expected_result['depth'], result['depth'])
        #self.assertEqual(expected_result['max_depth'], result['max_depth'])
        
    def test_move_up_blank_in_first_row(self):
        initial = PuzzleState([0,1,2,3,4,5,6,7,8], 3)
        self.assertIsNone(initial.move_up())
        
        initial = PuzzleState([1,0,2,3,4,5,6,7,8], 3)
        self.assertIsNone(initial.move_up())
        
        initial = PuzzleState([1,2,0,3,4,5,6,7,8], 3)
        self.assertIsNone(initial.move_up())
        
    def test_move_up_blank_in_second_row(self):
        initial = PuzzleState([1,2,3,0,4,5,6,7,8], 3)
        self.assertEqual(initial.move_up().config, [0,2,3,1,4,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,0,5,6,7,8], 3)
        self.assertEqual(initial.move_up().config, [1,0,3,4,2,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,5,0,6,7,8], 3)
        self.assertEqual(initial.move_up().config, [1,2,0,4,5,3,6,7,8])

    def test_move_up_blank_in_third_row(self):
        initial = PuzzleState([1,2,3,4,5,6,0,7,8], 3)
        self.assertEqual(initial.move_up().config, [1,2,3,0,5,6,4,7,8])
        
        initial = PuzzleState([1,2,3,4,5,6,7,0,8], 3)
        self.assertEqual(initial.move_up().config, [1,2,3,4,0,6,7,5,8])
        
        initial = PuzzleState([1,2,3,4,5,6,7,8,0], 3)
        self.assertEqual(initial.move_up().config, [1,2,3,4,5,0,7,8,6])
        
    def test_move_down_blank_in_first_row(self):
        initial = PuzzleState([0,1,2,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_down().config, [3,1,2,0,4,5,6,7,8])
        
        initial = PuzzleState([1,0,2,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_down().config, [1,4,2,3,0,5,6,7,8])
        
        initial = PuzzleState([1,2,0,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_down().config, [1,2,5,3,4,0,6,7,8])
        
    def test_move_down_blank_in_second_row(self):
        initial = PuzzleState([1,2,3,0,4,5,6,7,8], 3)
        self.assertEqual(initial.move_down().config, [1,2,3,6,4,5,0,7,8])
        
        initial = PuzzleState([1,2,3,4,0,5,6,7,8], 3)
        self.assertEqual(initial.move_down().config, [1,2,3,4,7,5,6,0,8])
        
        initial = PuzzleState([1,2,3,4,5,0,6,7,8], 3)
        self.assertEqual(initial.move_down().config, [1,2,3,4,5,8,6,7,0])

    def test_move_down_blank_in_third_row(self):
        initial = PuzzleState([1,2,3,4,5,6,0,7,8], 3)
        self.assertIsNone(initial.move_down())
        
        initial = PuzzleState([1,2,3,4,5,6,7,0,8], 3)
        self.assertIsNone(initial.move_down())
        
        initial = PuzzleState([1,2,3,4,5,6,7,8,0], 3)
        self.assertIsNone(initial.move_down())
        
    def test_move_blank_left_in_left_col(self):
        initial = PuzzleState([0,1,2,3,4,5,6,7,8], 3)
        self.assertIsNone(initial.move_left())
        
        initial = PuzzleState([1,2,3,0,4,5,6,7,8], 3)
        self.assertIsNone(initial.move_left())
        
        initial = PuzzleState([1,2,3,4,5,6,0,7,8], 3)
        self.assertIsNone(initial.move_left())
        
    def test_move_blank_left_in_middle_col(self):
        initial = PuzzleState([1,0,2,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_left().config, [0,1,2,3,4,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,0,5,6,7,8], 3)
        self.assertEqual(initial.move_left().config, [1,2,3,0,4,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,5,6,7,0,8], 3)
        self.assertEqual(initial.move_left().config, [1,2,3,4,5,6,0,7,8])

    def test_move_blank_left_in_right_col(self):
        initial = PuzzleState([1,2,0,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_left().config, [1,0,2,3,4,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,5,0,6,7,8], 3)
        self.assertEqual(initial.move_left().config, [1,2,3,4,0,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,5,6,7,8,0], 3)
        self.assertEqual(initial.move_left().config, [1,2,3,4,5,6,7,0,8])
        
    def test_move_blank_right_in_left_col(self):
        initial = PuzzleState([0,1,2,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_right().config, [1,0,2,3,4,5,6,7,8])
        
        initial = PuzzleState([1,2,3,0,4,5,6,7,8], 3)
        self.assertEqual(initial.move_right().config, [1,2,3,4,0,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,5,6,0,7,8], 3)
        self.assertEqual(initial.move_right().config, [1,2,3,4,5,6,7,0,8])
        
    def test_move_blank_right_in_middle_col(self):
        initial = PuzzleState([1,0,2,3,4,5,6,7,8], 3)
        self.assertEqual(initial.move_right().config, [1,2,0,3,4,5,6,7,8])
        
        initial = PuzzleState([1,2,3,4,0,5,6,7,8], 3)
        self.assertEqual(initial.move_right().config, [1,2,3,4,5,0,6,7,8])
        
        initial = PuzzleState([1,2,3,4,5,6,7,0,8], 3)
        self.assertEqual(initial.move_right().config, [1,2,3,4,5,6,7,8,0])

    def test_move_blank_right_in_right_col(self):
        initial = PuzzleState([1,2,0,3,4,5,6,7,8], 3)
        self.assertIsNone(initial.move_right())
        
        initial = PuzzleState([1,2,3,4,5,0,6,7,8], 3)
        self.assertIsNone(initial.move_right())
        
        initial = PuzzleState([1,2,3,4,5,6,7,8,0], 3)
        self.assertIsNone(initial.move_right())
        
    def test_manhattan_dist(self):
        index, value = 0, 0
        self.assertEqual(calculate_manhattan_dist(index, value, None), 0)
        
        index, value = 1, 0 # test needed left move
        self.assertEqual(calculate_manhattan_dist(index, value, None), 1)
        
        index, value = 0, 2 # test needed right move
        self.assertEqual(calculate_manhattan_dist(index, value, None), 2)
        
        index, value = 8, 2 # test needed up move
        self.assertEqual(calculate_manhattan_dist(index, value, None), 2)
        
        index, value = 3, 6 # test needed down move
        self.assertEqual(calculate_manhattan_dist(index, value, None), 1)
        
        # test combinations
        index, value = 0, 5
        self.assertEqual(calculate_manhattan_dist(index, value, None), 3)
        
        index, value = 5, 1
        self.assertEqual(calculate_manhattan_dist(index, value, None), 2)
        
        index, value = 2, 6
        self.assertEqual(calculate_manhattan_dist(index, value, None), 4)
        
        index, value = 3, 2
        self.assertEqual(calculate_manhattan_dist(index, value, None), 3)
        
if __name__ == '__main__':
    unittest.main()