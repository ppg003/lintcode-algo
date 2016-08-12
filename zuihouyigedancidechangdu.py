def lengthOfLastWord(s):
    """
    :param s: s A string
    :return: the length of last word
    """

    length = len(s)

    if length == 0:
        return 0

    if s[length - 1] != " ":
        for i in range(length - 1, -1, -1):
            length_last_word = length - 1 - i
            if s[i] == " ":
                return length_last_word
        return length
    else:
        for i in range(length - 1, -1, -1):
            if s[i] != " ":
                for j in range(i, -1, -1):
                    length_last_word = i - j
                    if s[j] == " ":
                        return length_last_word
        return 0


print(lengthOfLastWord(" vboImaga"))