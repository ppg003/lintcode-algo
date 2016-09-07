class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        if s == []:
            return s
        length = len(s)
        offset %= length
        n = length - offset
        tmp = s[n:]
        for i in range(n - 1, -1, -1):
            s[i + offset] = s[i]

        for i in range(0, offset):
            s[i] = tmp[i]
        return s


s = list("abcdefg")
offset = 3
x = Solution()
print(x.rotateString(s, offset))
