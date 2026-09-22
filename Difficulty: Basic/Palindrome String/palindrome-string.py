class Solution:
    def isPalindrome(self, s):
        new_string = ''
        l = len(s)
        for i in range(l-1,-1,-1):
            new_string = new_string+s[i]
        if s == new_string:
            return True
        else:
            return False