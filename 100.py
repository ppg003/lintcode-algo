class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        length = len(A)
        if length in [0, 1]:
            return length
        i = 1
        while i < length:
            if A[i] == A[i - 1]:
                del A[i]
                length -= 1
            else:
                i += 1
        return length

x = Solution()
data = [1, 1, 2, 4, 4, 5]
print(x.removeDuplicates(data))