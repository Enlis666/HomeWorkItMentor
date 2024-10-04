from binary_search import binary_search
from bubble_sort import bubble_sort
import unittest


class TestSort(unittest.TestCase):
    def setUp(self):
        self.array_binary = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.array_bubble = [81, 50, 4, 27, 34, 5, 90]
        self.correct_bubble_sort = [4, 5, 27, 34, 50, 81, 90]
        self.target_binary = 1

    def test_binary_search(self):
        self.assertEqual(binary_search(self.array_binary, self.target_binary), 0)


    def test_bubble_sort(self):
        result = bubble_sort(self.array_bubble)
        self.assertEqual(result, self.correct_bubble_sort)

if __name__ == '__main__':
    unittest.main()