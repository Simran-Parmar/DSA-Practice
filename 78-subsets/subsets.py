class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        result = []
        for i in range(0, 2**n):
            temp = []
            for k in range(0,n):
                if i & (1<<k) != 0:
                    temp.append(nums[k])
            result.append(temp)
        return result    