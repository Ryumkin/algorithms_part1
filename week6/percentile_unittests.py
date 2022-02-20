from random import seed

from numpy.random import randint
from percentile import find_percentile, find_percentile_initial_approach
import unittest


class UnitTests(unittest.TestCase):

    def test_b_is_empty_should_return(self):
        answer = find_percentile([1, 2, 4], [], 50)
        expected_answer = 2
        self.assertEqual(expected_answer, answer)

    def test_a_is_empty_should_return(self):
        answer = find_percentile([], [1, 2, 4], 50)
        expected_answer = 2
        self.assertEqual(expected_answer, answer)

    def test_median(self):
        test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
        self.assertEqual(7, find_percentile(test_a, test_b, test_p),
                         "should_be_7")

    def test_percentile(self):
        test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
        self.assertEqual(20, find_percentile(test_a, test_b, test_p),
                         "should_be_20")


def create_random_array(max_length=100, max_number=1000):
    seed(1)
    return sorted(randint(0, randint(1, max_number), randint(1, max_length)))


def create_array(max_length=100, max_number=1000):
    seed(1)
    return sorted(randint(0, max_number, max_length))


class StressTests(unittest.TestCase):

    def test_with_naive(self):
        for i in range(100):
            a, b = create_random_array(), create_random_array()
            p = int(randint(1, 100)) % 100
            expected_answer = find_percentile_initial_approach(a, b, p)
            answer = find_percentile(a, b, p)
            self.assertEqual(expected_answer, answer, f"a={a}, \n b {b} \n p {p}")


class MaxTests(unittest.TestCase):

    def test_with_naive(self):
        a, b = create_array(1000000, 10000000), create_array(1000000, 10000000)
        p = int(randint(1, 100)) % 100
        expected_answer = find_percentile_initial_approach(a, b, p)
        answer = find_percentile(a, b, p)
        self.assertEqual(expected_answer, answer, f"a={a}, \n b {b} \n p {p}")


if __name__ == '__main__':
    unittest.main()
