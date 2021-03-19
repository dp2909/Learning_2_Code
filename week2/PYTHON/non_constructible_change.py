#!/usr/bin/env python3

"""
Non-Constructible Change:

Given an array of positive integers representing the values
of coins in your possession, write a function that returns the minimum
amount of change (the minimum sum of money) that you cannot create.
The given coins can have any positive integer value and aren't 
necessarily unique (you can have multiple of the same coin).

For example, if you're given coins = [1,2,5], the minimum amount of
change that you can't create is 4 (1+2 = 3, 1+5=6, 2+5=7). If you
are given no coins, the minimum amount of change that you can't
create is 1.

Sample Input:

coins = [5, 7, 1, 1, 2, 3, 22]

Sample Output:
20

Note + Hint: You cannot use any built-in sorting algorithms to solve this.
Note + Hint: You may need to add a second function (your sorting function) to this
             exercise, and call it in your non_constructible_change function.

Optimal Space and Time Complexity:

O(NlogN) time | O(1) space - where n is the number of coins

Reasonable Space and Time complexity:

O (N^2) time | O(1) space
"""

import unittest

def non_constructible_change(coins):
    # Your code goes here
    pass

# Do not modify anything below this point, these are test cases!!!!

class TestNonConstructibleChange(unittest.TestCase):
    def setUp(self):
        self.input_coins = [[5, 7, 1, 1, 2, 3, 22],
                            [1,1,1,1,1],
                            [1, 5, 1, 1, 1, 10, 15, 20, 100],
                            [6, 4, 5, 1, 1, 8, 9],
                            [],
                            [87]]
        self.result = [20, 6, 55, 3, 1, 1]
        
    def test_data(self):
        count = 1
        for in_coins, res in zip(self.input_coins, self.result):
            actual_result = non_constructible_change(in_coins)
            if actual_result == res:
                status = "SUCCESS"
            else:
                status = "FAIL"
            print("Test %i:" %count, in_coins, ",", "Expected_result: %i" %res, "," "Actual Result: ", actual_result, ",", "Status: %s" %status)
            count += 1

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
