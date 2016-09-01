class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):

        if n <= 2:
            return k ** n

        if k <= 1:
            return 0

        ways = (self.numWays(n - 2, k) + self.numWays(n - 1, k)) * (k - 1)
        return ways


x = Solution()
print(x.numWays(10, 3))
