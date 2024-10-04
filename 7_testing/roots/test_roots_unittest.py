import unittest
from roots import square_eq_solver

class SquareEqSolverTestCase(unittest.TestCase):
   def test_no_root(self):
       res = square_eq_solver(10, 0, 2)
       self.assertEqual(len(res), 0)

   def test_single_root(self):
       res = square_eq_solver(10, 0, 0)
       self.assertEqual(len(res), 1)
       self.assertEqual(res, [0])

   def test_multiple_root(self):
       res = square_eq_solver(2, 5, -3)
       self.assertEqual(len(res), 2)
       self.assertEqual(res, [0.5, -3])
