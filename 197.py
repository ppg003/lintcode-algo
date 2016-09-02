class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        def __posibility(n):
            if n == 1 or n == 2:
                return n
            res = 2
            for i in range(3, n + 1):
                res *= i
            return res

        B = A[:]
        B.sort()

        res = 0

        for i in range(len(A)):
            n = B.index(A[i])
            res += n * __posibility(len(A) - i - 1)
            B.remove(A[i])

        res += 1

        return res


A = [1, 3, 4, 2]
x = Solution()
print(x.permutationIndex(A))
