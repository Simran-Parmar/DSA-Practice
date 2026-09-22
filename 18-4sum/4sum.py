class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        result = []
        nums.sort()
        for i in range(0,n-2):
            if i !=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-1):
                if j != i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]<target:
                        k = k+1
                    elif nums[i]+nums[j]+nums[k]+nums[l]>target:
                        l = l-1
                    else:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        result.append(temp)
                        k = k+1
                        l = l-1
                        while nums[k]==nums[k-1] and k<l:
                            k = k+1
                        while nums[l]==nums[l+1] and k<l:
                            l = l-1
        return result






        