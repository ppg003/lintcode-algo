class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):

        def iscm2(num):
            if num % 2 == 0:
                return True
            return False

        def iscm5(num):
            if num % 5 == 0:
                return True
            return False

        def iscm10(num):
            if num % 10 == 0:
                return True
            return False

        count = 0
        cm2 = 0
        cm5 = 0
        for i in range(1, n + 1):
            if iscm10(i):
                count += 1
            else:
                if iscm2(i):
                    if cm5 > 0:
                        cm5 -= 1
                        count += 1
                    else:
                        cm2 += 1
                if iscm5(i):
                    if cm2 > 0:
                        cm2 -= 1
                        count += 1
                    else:
                        cm5 += 1
        return count

n = 24
x = Solution()
print(x.trailingZeros(n))