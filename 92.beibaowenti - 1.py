def backPack(m, A):
    """
    :param m: An integer m denotes the size of a backpack
    :param A: Given n items with size A[i]
    :return: The maximum size
    """
    length = len(A)
    A2 = A[1:]
    m2 = m - A[0]
    print("A : %s" % A)
    print("A2 : %s" % A2)
    print("m : %s" % m)
    print("m2 : %s" % m2)
    print("A[0] : %s" % A[0])

    if length == 1:
        if A[0] <= m:
            return A[0]
        else:
            return 0

    if backPack(m2, A2) + A[0] >= backPack(m, A2):
        size_max = backPack(m2, A2) + A[0]
        print(size_max)
        print("add %s" % A[0])
    else:
        size_max = backPack(m, A2)

    return size_max


A = [7, 5, 3, 2]
m = 12
print(backPack(m, A))

