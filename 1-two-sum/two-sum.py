class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        r = 0
        for i in range(0,len(nums)):
            r = target - nums[i]
            if r in d:
                return [i,d[r]]
            d[nums[i]] = i
