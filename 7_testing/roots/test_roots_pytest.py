import pytest

from roots import square_eq_solver


def test_no_root():
   res = square_eq_solver(10, 0, 2)
   assert len(res) == 0

def test_single_root():
   res = square_eq_solver(10, 0, 0)
   assert len(res) == 1
   assert res == [0]

def test_multiple_root():
   res = square_eq_solver(2, 5, -3)
   assert len(res) == 3
   assert res == [0.5, -3]