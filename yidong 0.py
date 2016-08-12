def moveZeroes(nums):
    length_nums = len(nums)
    i = 0
    if length_nums in [0, 1]:
        return nums
    while i < length_nums:
        if nums[i] == 0:
            all_0 = True
            for k in range(i, length_nums):
                print(nums[k])
                if nums[k] != 0:
                    all_0 = False
            print(all_0)
            if all_0 == False:
                j = length_nums - 1
                temp_1 = nums[j]
                print(j)
                nums[j] = 0
                while j > i:
                    j -= 1
                    temp_2 = nums[j]
                    nums[j] = temp_1
                    temp_1 = temp_2
            else:
                return nums
        else:
            i += 1
    return nums


print(moveZeroes([0, -4]))
