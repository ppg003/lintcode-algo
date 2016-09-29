class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        index_base = 0
        while len(nums)>1:
            index = int(len(nums) / 2) - 1
            nums_l = nums[:index + 1]
            nums_r = nums[index + 1:]
            if nums[index] >= target:
                if nums[index] == target:
                    if index == 0:
                        return index_base
                    if nums[index - 1] != target:
                        return index + index_base
                nums = nums_l
            else:
                index_base += index + 1
                nums = nums_r

        return -1


nums = [2, 2, 3, 4, 5, 6, 8, 13, 17, 18]
target = 17
x = Solution()
print(x.binarySearch(nums, target))