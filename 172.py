class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        length = len(A)
        if length == 0:
            return 0
        i = 0
        while i < length:
            if A[i] == elem:
                del A[i]
                length -= 1
            else:
                i += 1
        return length


x = Solution()
A = [0, 4, 4, 0, 0, 2, 4, 4]
elem = 4
print(x.removeElement(A, elem))
