from puzzle import PuzzleState, calculate_manhattan_dist
import unittest

class TestPuzzleMethods(unittest.TestCase):
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