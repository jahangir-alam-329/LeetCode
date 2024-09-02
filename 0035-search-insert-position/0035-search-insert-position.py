class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l=len(nums)
        for i in range(0,l):
            if(nums[i]==target):
                return i
        for i in range(0,l-1):
            if(nums[i] < target) and (target < nums[i+1]):
                    return i+1
        if(nums[0]>target):
            return 0
        if(nums[l-1]<target):
            return l

        