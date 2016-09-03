class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """

    def minSubArray(self, nums):
        if nums == []:
            return 0

        length = len(nums)
        min_cache = []
        for i in range(length):
            if i == 0:
                min_cache.append(nums[i])
            else:
                min_cache.append(min(min_cache[i- 1] + nums[i], nums[i]))

        return min(min_cache)

nums = [1, -1, -2, 1]

nums2 = [-5, 10, -20, 6, -10, 6, -5]
nums3 = [1, 2, 3, 4, 5, 6, 7]
x = Solution()
print(x.minSubArray(nums2))
