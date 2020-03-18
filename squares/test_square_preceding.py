import unittest
from squares.square_preceding import square_preceding


class TestPoint(unittest.TestCase):
    def test_edge_case(self):
        l = [1, 2, 3]
        square_preceding(l)
        self.assertEqual(l, [0, 1, 4])

        l = []
        square_preceding(l)
        self.assertEqual(l, [])


if __name__ == '__main__':
    unittest.main()
