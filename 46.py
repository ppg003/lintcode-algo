class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """

    def majorityNumber(self, nums):
        dict = {}
        length = len(nums)
        for num in nums:
            if num not in dict.keys():
                dict[num] = 1
            else:
                dict[num] += 1

            if dict[num] > float(length) / 2:
                return num

        return None


nums = [1, 1, 1, 1, 2, 2, 2]
x = Solution()
print(x.majorityNumber(nums))
