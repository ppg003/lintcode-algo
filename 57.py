class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        numbers.sort()
        length = len(numbers)
        cur_1 = 0

        # print(numbers)
        res = []

        count_0 = 0
        for num in numbers:
            if num == 0:
                count_0 += 1

        if count_0 >= 3:
            res.append([0, 0, 0])

        while numbers[cur_1] < 0:
            cur_2 = length - 1
            while numbers[cur_2] > 0:
                # print("cur_1 : %s cur_2 : %s" % (cur_1, cur_2))
                # print("cur_1 value : %s cur_2 value: %s" % (numbers[cur_1], numbers[cur_2]))
                if numbers[cur_1] + numbers[cur_2] == 0:
                    if count_0 > 0:
                        if [numbers[cur_1], 0, numbers[cur_2]] not in res:
                            res.append([numbers[cur_1], 0, numbers[cur_2]])
                        # print("+")
                    cur_2 -= 1
                    continue

                if numbers[cur_1] + numbers[cur_2] < 0:
                    cur_3 = cur_2 - 1
                    while numbers[cur_3] > 0:
                        if numbers[cur_2] + numbers[cur_3] + numbers[cur_1] == 0 and [numbers[cur_1], numbers[cur_3], numbers[cur_2]] not in res:
                            # print(numbers[cur_3])
                            res.append([numbers[cur_1], numbers[cur_3], numbers[cur_2]])
                            # print("+")
                            break
                        cur_3 -= 1
                    cur_2 -= 1
                    continue
                else:
                    cur_3 = cur_1 + 1
                    while numbers[cur_3] < 0:
                        if numbers[cur_2] + numbers[cur_3] + numbers[cur_1] == 0 and [numbers[cur_1], numbers[cur_3], numbers[cur_2]] not in res:
                            # print(numbers[cur_3])
                            res.append([numbers[cur_1], numbers[cur_3], numbers[cur_2]])
                            # print("+")
                            break
                        cur_3 += 1
                    cur_2 -= 1
                    continue
            cur_1 += 1
        return res

numbers = [-1, 0, 1, 2, -1, -4]
x = Solution()
print(x.threeSum(numbers))





