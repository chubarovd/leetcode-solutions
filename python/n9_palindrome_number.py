class Solution(object):
    def my_isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        xstr = str(x)
        xlen = len(xstr) - 1
        for i in range(0, xlen + 1):
            if i >= (xlen - i):
                return True
            if xstr[i] != xstr[xlen - i]:
                return False

    def best_isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        half = 0
        while half < x:
            half = (10 * half) + (x % 10)
            x //= 10
        if half == x or half // 10 == x:
            return True
        return False


sln = Solution()
print(sln.best_isPalindrome(121))
