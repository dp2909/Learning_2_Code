# Week2 Python Problems

This readme will be much less involved, I'll post a few practice algorithm problems in python, and you attempt to solve them for all test cases.

Remember the steps:

1. I assume you are already on the week2 branch (from main, `git checkout week2`)
2. create a new branch: `git branch dev_week2_solns`
3. switch to it: `git checkout dev_week2_solns`
4. copy your attempts, and we will discuss

I will assert correctness differently this week as the tests are designed to be a little harder.

Basically, I'll be adding unittests to the code, so I don't have to eyeball it. This way, I can easily know what passes and fails.

I have setup the test cases in such a way that you can run the code like this:

```
python3 two_numbers_sum.py

Test 1:  [3, 5, -4, 8, 11, 1, -1, 6] , 10 , Expected Result:  True , Actual Result:  None , Status: FAIL
Test 2:  [4, 6] , 10 , Expected Result:  True , Actual Result:  None , Status: FAIL
Test 3:  [4, 6, 1] , 5 , Expected Result:  True , Actual Result:  None , Status: FAIL
Test 4:  [4, 6, 1, -3] , 3 , Expected Result:  True , Actual Result:  None , Status: FAIL
Test 5:  [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47] , 163 , Expected Result:  True , Actual Result:  None , Status: FAIL
Test 6:  [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47] , 164 , Expected Result:  False , Actual Result:  None , Status: FAIL
Test 7:  [3, 5, -4, 8, 11, 1, -1, 6] , 15 , Expected Result:  False , Actual Result:  None , Status: FAIL
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

You can see the test number, the inputs, the expected result, and the actual result from left to right.
