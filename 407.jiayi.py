def plusOne(digits):
    """
    :param digits: a number represented as an array of digits
    :return: the result
    """
    length = len(digits)
    total = 0
    for i in range(length):
        total += digits[i] * 10 ** (length - i - 1)
    total += 1
    total = list(str(total))
    total = list(map(lambda x: int(x), total))
    return total


x = [9, 9, 9]
print(plusOne(x))
