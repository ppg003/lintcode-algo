# http://www.lintcode.com/zh-cn/problem/reverse-words-in-a-string/

def reverseWords(s):
    """
    :param s: A string
    :return: A string
    """
    length = len(s)
    list_word = []
    i = 0
    while i < length:
        if s[i] != " ":
            for j in range(i + 1, length):
                if s[j] == " ":
                    index_end_letter = j - 1
                    list_word.append(s[i:index_end_letter + 1])
                    i += len(s[i:index_end_letter + 1])
                    break
                elif j == length - 1:
                    index_end_letter = j
                    list_word.append(s[i:index_end_letter + 1])
                    i += len(s[i:index_end_letter + 1])
        else:
            i += 1
    res = ""
    for i in range(len(list_word) -1, -1, -1):
        res += list_word[i]
        if i != 0:
            res += " "
    return res


print(reverseWords("the    sky is   blue   "))