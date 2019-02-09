import unittest
from algorithms.triplets import Solution


class TripletsTest(unittest.TestCase):
    def test_empty(self):
        result = Solution().get_triplets([])
        self.assertEqual([], result, msg="should be empty")

    def test_none(self):
        result = Solution().get_triplets([-1, -2, -6, -9])
        self.assertEqual([], result, msg="should be empty")

    def test_2_dim(self):
        result = Solution().get_triplets([0, 0])
        self.assertEqual([], result, msg="should be empty")

    def test_2_dim_2(self):
        result = Solution().get_triplets([0, 1])
        self.assertEqual([], result, msg="should be empty")

    def test_demo(self):
        S = [-4, -2, -1, 0, 1, 3, 4]
        solution = [[-4, 1, 3], [-4, 0, 4], [-2, -1, 3], [-1, 0, 1]]
        solution.sort()

        result = Solution().get_triplets(S)
        self.assertEqual(solution, result, msg="should be equal")


if __name__ == '__main__':
    unittest.main()
