class Solution(object):
    def isPalindrome(self, x):
        x=True if str(x)==str(x)[::-1] else False
        return x
