class Solution(object):
    def subsets(self,nums):
        result = []
        def helper(nums,result,indx,stack):
            if indx == len(nums):
                result.append(stack[:])
                return 
            helper(nums,result,indx+1,stack)
            stack.append(nums[indx])
            helper(nums,result,indx+1,stack)
            stack.pop()
        helper(nums,result,0,[])
        return result
























    # BY BIT MANIPULATION
        # n = len(nums)
        # result = []
        # for i in range(0, 2**n):
        #     temp = []
        #     for k in range(0,n):
        #         if i & (1<<k) != 0:
        #             temp.append(nums[k])
        #     result.append(temp)
        # return result    
