from puzzle import PuzzleState
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
        
if __name__ == '__main__':
    unittest.main()