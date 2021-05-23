class Solution(object):
    def my_reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ten_pows = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
        absx = abs(x)
        ind = -1
        for i in range(0, 10):
            if absx // ten_pows[i] > 0:
                ind = i
        if ind == -1:
            return x
        answer = absx // ten_pows[ind]
        for i in range(0, ind + 1):
            print(i)
            answer += ten_pows[ind - i] * (absx % 10)
            absx //= 10
        if x < 0:
            answer = -answer
        if answer < - 2 ** 31 or answer > 2 ** 31 - 1:
            return 0
        return answer

    # when submitted it, runtime was more than my solution gives...
    # but it shows best result in submission details, why ???
    def best_reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = ""
        negative = False
        if (x < 0):
            x = -x
            negative = True
        num = str(x)
        for c in num:
            out = c + out

        output = int(out)
        if (negative):
            output = -output

        if (output > -2 ** 31 and output < 2 ** 31 - 1):
            return output
        else:
            return 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False
        if x < 0:
            x = -x
            is_negative = True
        ans = 0
        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10
        if -2 ** 31 <= ans <= 2 ** 31 - 1:
            if is_negative:
                return -ans
            else:
                return ans
        return 0


sln = Solution()
print(sln.reverse(0))
