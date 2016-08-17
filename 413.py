class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        if n == 0:
            return 0
        str_n = str(n)

        if n > 0:
            length = len(str_n)
            res = ""
            for i in range(length - 1, -1, -1):
                res += str_n[i]

            res = int(res)
            if res > 2 ** 32:
                return 0

            return res

        if n < 0:
            length = len(str_n)
            res = ""
            for i in range(length - 1, 0, -1):
                res += str_n[i]

            res = -(int(res))
            if res < -2 ** 32:
                return 0

            return res
