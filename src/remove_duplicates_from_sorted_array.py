from typing import List
from datetime import datetime as dt


class SolutionZ:

    def removeDuplicates(self, nums: List[int]) -> int:

        def dedup(nums, unique, i):
            if len(nums) == i:
                return i, nums

            if unique >= nums[i]:
                nums[i] = -1
                return dedup(nums, unique, i + 1)
            return i, nums

        i = 0
        unique_index = 0

        if len(nums) <= 1:
            return len(nums)

        while len(nums) >= i + 1:
            if (unique_index != i) and (nums[unique_index] == nums[i]):
                if len(nums) > 1 and i == 0:
                    nums[i + 1] = -1
                else:
                    nums[i] = -1

                i, nums = dedup(nums, nums[unique_index], i + 1)

            if (len(nums) != i) and (nums[unique_index] < nums[i]):
                p = nums[unique_index + 1]
                nums[unique_index + 1] = nums[i]
                nums[i] = p
                unique_index += 1

            i += 1
        # print(f"\t{self.removeDuplicates.__name__}:{nums}")
        nums = nums[:(unique_index + 1)]
        return len(nums)


class SolutionA:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0

        target_index = 1
        first = nums[0]
        i = 1
        while len(nums) > i:
            if nums[i] != first:
                first = nums[i]
                nums[target_index] = nums[i]
                target_index += 1
            i += 1

        # print(f"\t{self.removeDuplicates2.__name__}:{nums}")
        return target_index


if __name__ == '__main__':

    tests = [[1, 2, 3],
             [1, 2],
             [0],
             [0, 0],
             [1, 1, 1],
             [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
             [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4],
             [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9],
             [1, 1, 2],
             [0, 1, 1, 2]
             ]
    for index, arr in enumerate(tests):
        print(f"Input: {arr}")
        solutions = {
            "solution Z": SolutionZ().removeDuplicates,
            "solution A": SolutionZ().removeDuplicates,
        }
        for s, f in solutions.items():
            start = dt.now()
            print(f"{index}:{f(arr)},\t{s}\ttime:{dt.now() - start}")
