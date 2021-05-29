dct = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def my_romanToInt(self, s: str) -> int:
        numb = 0
        c_prev = ''
        for c in reversed(s):
            if c == 'I':
                if c_prev == 'V' or c_prev == 'X':
                    numb -= 1
                else:
                    numb += 1
            elif c == 'V':
                numb += 5
            elif c == 'X':
                if c_prev == 'L' or c_prev == 'C':
                    numb -= 10
                else:
                    numb += 10
            elif c == 'L':
                numb += 50
            elif c == 'C':
                if c_prev == 'D' or c_prev == 'M':
                    numb -= 100
                else:
                    numb += 100
            elif c == 'D':
                numb += 500
            else:
                numb += 1000
            c_prev = c
        return numb


sln = Solution()
print(sln.romanToInt('MCMXCIV'))
