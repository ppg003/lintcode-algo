class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return true or false
    """

    def anagram(self, s, t):
        s = list(s)
        t = list(t)
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        for elem in t:
            if elem in s:
                s.remove(elem)

        if not s:
            return True

        return False

s = "cab"
t = "abc"
x = Solution()
print(x.anagram(s, t))