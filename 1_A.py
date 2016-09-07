class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """

    def aplusb(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a

        x1 = a ^ b
        x2 = (a & b) << 1
        return self.aplusb(x1, x2)


a = 1
b = 2
x = Solution()
print(x.aplusb(a, b))
