class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        i = 0
        while 1:
            if i ** 2 <= x < (i + 1) ** 2:
                return i
            i += 1


num = 28
x = Solution()
print(x.sqrt(num))
