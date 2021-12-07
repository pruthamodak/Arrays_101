### Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            check_even=0
            while(nums[i]//10!=0):
                nums[i]=nums[i]//10
                check_even=check_even+1
            if(check_even%2!=0):
                count=count+1
            check_even=0
        return count
