class Solution(object):
    def best_twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(0, len(nums)):
            check = dict.get(target - nums[i])
            if check is not None:
                return [check, i]
            dict[nums[i]] = i


sln = Solution()
print(sln.best_twoSum([1, 1, 1, 7, 7, 2, 7, 11, 15, 2], 9))
