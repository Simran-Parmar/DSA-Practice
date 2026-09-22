class Solution(object):
    def isPalindrome(self, s):
        new_s = []
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                new_s.append(ch)
        new_s = ''.join(new_s)
        l = 0
        r = len(new_s)-1
        for i in range (len(new_s)//2):
            if new_s[l] == new_s[r]:
                l = l+1
                r = r-1
            else:
                return False
        return True
        

