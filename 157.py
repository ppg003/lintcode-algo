class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):

        letter_hash = {}
        for letter in str:
            if letter in letter_hash.keys():
                return False
            letter_hash[letter] = ""

        return True

word = "abdcs"
x = Solution()
print(x.isUnique(word))