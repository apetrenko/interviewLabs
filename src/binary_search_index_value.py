from datetime import datetime as dt
from typing import List

"""Given an array A of sorted integers,
return the some value i so that A [i] = i  all the values are different
if there is no i, return null.

A = [0:-3,1:-1,2:1,3:2,4:3,5:4,6:7]
Result = null

A = [0:-1,1:1,2:1,3:2,4:3,5:4,6:7]
Result = 1

"""


class SolutionA:

    def get_result(self, nums: List[int]) -> int:
        def find_index(arr, start, end):
            if end >= 1:
                mid = start + (end - start) // 2
                if arr[mid] == mid:
                    return mid
                elif arr[mid] < mid:
                    return find_index(arr, mid + 1, end)
                else:
                    return find_index(arr, start, mid - 1)

        return find_index(nums, 0, len(nums) - 1)


class SolutionB:

    def get_result(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if i == v:
                return i


if __name__ == '__main__':

    test_cases = [[0, 1], [-1, 1], [-1, 0, 2], [-2, -1, 0, 3, 4, 7], [0, 1, 2, 3, 4, 7], [2, 3, 4]]

    for test_case_index, nums in enumerate(test_cases):
        print(f"Input {test_case_index}: {nums}")
        solutions = {
            "solution A": SolutionA().get_result,
            "solution B": SolutionB().get_result,
        }
        #TODO: two solutions give different result
        for name, f in solutions.items():
            start = dt.now()
            index = f(nums)
            end = dt.now()
            assert (index == nums[index] if index else True)
            print(f"\tResult[{name}]: {index} eq {nums[index] if index else None}\tfor\t{nums},\ttime:{end - start} ")
