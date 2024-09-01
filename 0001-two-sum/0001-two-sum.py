class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      l=len(nums)
      ans=[0,0]
      for i in range(0,l):
        for j in range(i+1,l):
          if nums[i]+nums[j]==target:
            ans[0]=i
            ans[1]=j
      return ans