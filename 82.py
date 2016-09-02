class Solution:
    """
    @param A : an integer array
    @return : a integer
    """

    def singleNumber(self, A):
        if A == []:
            return 0
        list = []
        for num in A:
            if num not in list:
                list.append(num)
            else:
                list.remove(num)
        return list[0]


A = [1, 2, 2, 1, 3, 4, 3]
x = Solution()
print(x.singleNumber(A))