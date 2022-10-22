import unittest
import MainProg
import time
import io
def provmult(a):
    mult=1
    for j in MainProg.numbers:
        mult*=j
    return(mult)

class TestsforProg(unittest.TestCase):
    def test_min_function(self):
        self.assertEqual(MainProg._min(MainProg.numbers), min(MainProg.numbers))

    def test_max_function(self):
        self.assertEqual(MainProg._max(MainProg.numbers), max(MainProg.numbers))

    def test_sum_function(self):
        self.assertEqual(MainProg._sum(MainProg.numbers), sum(MainProg.numbers))

    def test_max_function(self):
        self.assertEqual(MainProg._mult(MainProg.numbers), provmult(MainProg.numbers))
    def test_time(self):
        short_list_numbers = [1, 2, 3]
        start_time = time.time()
        MainProg._min(short_list_numbers)
        end_time = time.time()
        short_list_time = end_time - start_time

        long_list_numbers = [1, 2, 3]*1000
        start_time = time.time()
        MainProg._min(long_list_numbers)
        end_time = time.time()
        long_list_time = end_time - start_time
        self.assertAlmostEqual((short_list_time*1000 / long_list_time) >= 1, True)
if __name__ == '__main__':
    unittest.main