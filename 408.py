class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):

        length_a = len(a)
        length_b = len(b)

        i_a = length_a - 1
        i_b = length_b - 1

        res = ""
        cache = 0

        while i_a >= 0 and i_b >= 0:
            sum = int(a[i_a]) + int(b[i_b]) + cache
            if sum in [2, 3]:
                cache = 1
            else:
                cache = 0

            num = sum % 2

            res = str(num) + res
            i_a -= 1
            i_b -= 1

        if i_a == -1 and i_b == -1:
            if cache == 0:
                cache = ""
            return str(cache) + res

        if i_a >= 0:
            for i in range(i_a, -1, -1):
                sum = int(a[i]) + cache
                if sum == 2:
                    cache = 1
                else:
                    cache = 0
                num = sum % 2

                res = str(num) + res

            if cache == 1:
                res = str(cache) + res
            return res

        if i_b >= 0:
            for i in range(i_b, -1, -1):
                sum = int(b[i]) + cache
                if sum == 2:
                    cache = 1
                else:
                    cache = 0
                num = sum % 2

                res = str(num) + res

            if cache == 1:
                res = str(cache) + res
            return res


a = "11"
b = "111111"
x = Solution()
print(x.addBinary(a, b))
