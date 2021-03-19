#!/usr/bin/env python3

"""
Two Number Sum:

Write a function that takes in a non-empty array of distinct
integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum,
the function should return True (bool). If
no two numbers sum up to the target sum, the function should return
an False.

Note that the target sum has to be obtained by summing two different
integers in the array; you can't add a single integer to itself in 
order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up
to the target sum

Sample Input:

array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10

Sample Output:

[-1, 11]

Optimal Space and Time Complexity:

O(N) time | O(N) space - where n is the length of the input array
"""

import unittest

def two_number_sum(array, target_sum):
    # Your code goes here
    pass

# Do not modify anything below this point, these are test cases!!!!

class TestContainsSum(unittest.TestCase):
    def setUp(self):
        self.input_arrs = [[3, 5, -4, 8, 11, 1, -1, 6], [4,6], [4,6,1], [4,6,1,-3],
                           [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],
                           [3, 5, -4, 8, 11, 1, -1, 6]]
        self.input_sums = [10, 10, 5, 3, 163, 164, 15]
        self.results = [True, True, True, True, True, False, False]

    def test_data(self):
        count = 1
        for in_arr, in_sum, res in zip(self.input_arrs, self.input_sums, self.results):
            actual_result = two_number_sum(in_arr, in_sum)
            if actual_result == res:
                status = "SUCCESS"
            else:
                status = "FAIL"
            print("Test %i: "%count, in_arr, ",", in_sum, ",", "Expected Result: ", res, ",", "Actual Result: ", actual_result, ",", "Status: %s" %status)
            count += 1

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
