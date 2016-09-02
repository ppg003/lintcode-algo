class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1

        right = self.uniquePaths(m, n - 1)
        down = self.uniquePaths(m - 1, n)

        return down + right


class Solution2:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        table = [1 for i in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                table[j] += table[j - 1]

        return table[n - 1]


m = 3
n = 4
x = Solution2()
print(x.uniquePaths(m, n))
