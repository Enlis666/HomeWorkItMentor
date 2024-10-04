from scr.task_1 import main
import unittest

class TestMainFunction(unittest.TestCase):
    def setUp(self):
        self.correct_array_number = [
            1, 2, 4, 5, 10, 20, 25, 50, 73, 100, 137, 146, 274, 292, 365, 548, 685, 730, 1370, 1460, 1825, 2740,
            3425, 3650, 6850, 7300, 10001, 13700, 20002, 40004, 50005, 100010, 200020, 250025, 500050, 1000100
        ]
        self.correct_number = 1000100
        self.negative_number = 900

    def test1(self):
        self.assertEqual(main(self.correct_number), self.correct_array_number)

    def test2(self):
        self.assertNotEqual(main(self.negative_number), self.correct_array_number)


if __name__ == '__main__':
    unittest.main()