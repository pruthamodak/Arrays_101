### Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=[0]*len(nums)
        j=0
        for i in range(len(nums)):
            if(nums[i]==1):
                count[j]=count[j]+1
            if(i+1<len(nums) and nums[i+1]!=1):
                j=j+1
        return max(count)
