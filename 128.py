import time
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """

    def hashCode(self, key, HASH_SIZE):
        length = len(key)
        cache = 1
        sum = 0
        key10 = list(map(ord, key))

        for i in range(length):
            index = length - i - 1
            sum += key10[index] * cache
            cache = (cache * 33) % HASH_SIZE
        return sum % HASH_SIZE

with open("128_data", "r") as f:
    param = []
    for line in f.readlines():
        param.append(line)

param[0] = param[0].strip('\n')

key = param[0]
hs = int(param[1])
# key = "abcd"
# hs = 100
x = Solution()
start = time.clock()
print(x.hashCode(key, hs))
end = time.clock()
print(end - start)
