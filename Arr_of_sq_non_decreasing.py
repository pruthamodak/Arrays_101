### Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

import numpy as np

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=np.square(nums)
        return np.sort(nums)
