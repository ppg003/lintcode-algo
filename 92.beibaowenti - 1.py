def backPack(m, A):
    """
    :param m: An integer m denotes the size of a backpack
    :param A: Given n items with size A[i]
    :return: The maximum size
    """
    length = len(A)
    A2 = A[1:]
    m2 = m - A[0]
    # print("A : %s" % A)
    # print("A2 : %s" % A2)
    # print("m : %s" % m)
    # print("m2 : %s" % m2)
    # print("A[0] : %s" % A[0])

    if length == 1:
        if A[0] <= m:
            # print("add %s" % A[0])
            return A[0]
        else:
            return 0

    if A[0] > m:
        return backPack(m, A2)

    choice_1 = backPack(m2, A2) + A[0]
    choice_2 = backPack(m, A2)

    size_max = max([choice_1, choice_2])

    return size_max


A = [3, 4, 8, 5]
m = 10
print(backPack(m, A))

