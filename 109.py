class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """

    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]

        if len(triangle) == 2:
            return triangle[0][0] + min(triangle[1])

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[len(triangle) - 1])


class Solution2:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """

    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]

        if len(triangle) == 2:
            return triangle[0][0] + min(triangle[1])

        triangle_left = []
        for i in range(1, len(triangle)):
            triangle_left.append(triangle[i][:-1])

        triangle_right = []
        for i in range(1, len(triangle)):
            triangle_right.append(triangle[i][1:])

        max_sum = min(self.minimumTotal(triangle_left), self.minimumTotal(triangle_right))

        return triangle[0][0] + max_sum


t = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
x = Solution()
print(x.minimumTotal(t))
