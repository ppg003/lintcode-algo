class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if (n&(n-1)) == 0 and n > 0:
            return True
        return False