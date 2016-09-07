class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        import string
        length = len(s)
        char = string.ascii_lowercase + string.digits
        i = 0
        j = length - 1
        while i < j:
            cur_1 = s[i].lower()
            cur_2 = s[j].lower()
            while cur_1 not in char:
                i += 1
                if i == length:
                    return True
                cur_1 = s[i].lower()

            while cur_2 not in char:
                j -= 1
                if j == -1:
                    return True
                cur_2 = s[j].lower()

            if cur_1 != cur_2:
                return False

            i += 1
            j -= 1

        return True

s = "A man, a plan, a canal: Panama"
s2 = ".,"
x = Solution()
print(x.isPalindrome(s2))


