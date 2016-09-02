class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        if num <= 0:
            return False

        def __can_divi(num):
            if num % 2 == 0:
                return 2
            if num % 3 == 0:
                return 3
            if num % 5 == 0:
                return 5
            return 0

        while __can_divi(num) != 0:
            num /= __can_divi(num)

        if num != 1:
            return False
        return True

num = 123456
x = Solution()
print(x.isUgly(num))
