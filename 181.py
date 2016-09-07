class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):

        def ten2two(num, length):
            base = int("1" * length, 2)
            res = bin(num & base)[2:].rjust(length, "0")
            return res

        bi_a = ten2two(a, 32)
        bi_b = ten2two(b, 32)

        diff = 0
        for i in range(len(bi_a)):
            if bi_a[i] != bi_b[i]:
                diff += 1

        return diff




a = 1
b = -1
x = Solution()
print(x.bitSwapRequired(a, b))