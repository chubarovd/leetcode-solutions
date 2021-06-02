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
        for i in range(len(s)):
            if s[i] == 'I':
                if s[i + 1] == 'V' or s[i + 1] == 'X':
                    numb -= 1
                    i += 1
                else:
                    numb += 1
            elif s[i] == 'V':
                numb += 5
            elif s[i] == 'X':
                if s[i + 1] == 'L' or s[i + 1] == 'C':
                    numb -= 10
                    i += 1
                else:
                    numb += 10
            elif s[i] == 'L':
                numb += 50
            elif s[i] == 'C':
                if s[i + 1] == 'D' or s[i + 1] == 'M':
                    numb -= 100
                    i += 1
                else:
                    numb += 100
            elif s[i] == 'D':
                numb += 500
                i += 1
            else:
                numb += 1000
        return numb


sln = Solution()
print(sln.my_romanToInt('IX'))
