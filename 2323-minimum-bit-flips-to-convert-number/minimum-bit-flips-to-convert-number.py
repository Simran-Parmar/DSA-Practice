class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        count = 0
        while ans > 0:
            remainder = ans%2
            if remainder == 1:
                count = count + 1
            ans = ans//2
        return count
            

        