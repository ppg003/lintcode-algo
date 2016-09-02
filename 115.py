class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0 for j in range(n)] for i in range(m)]

        for column in range(n):
            if obstacleGrid[0][column] == 0:
                table[0][column] = 1
            else:
                break

        for row in range(m):
            if obstacleGrid[row][0] == 0:
                table[row][0] = 1
            else:
                break

        for row in range(1, m):
            for column in range(1, n):
                if obstacleGrid[row][column] == 1:
                    table[row][column] = 0
                else:
                    table[row][column] = table[row - 1][column] + table[row][column - 1]

        return table[m - 1][n - 1]
