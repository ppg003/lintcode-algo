class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        length = len(nums)
        if length in (0, 1):
            return nums

        index = 0

        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                index = i
                break

        if index != 0:
            nums.extend(nums[:i])
            for j in range(index):
                del nums[0]
        return nums

nums = [4, 5, 6, 1, 2, 3]
x = Solution()
print(x.recoverRotatedSortedArray(nums))
