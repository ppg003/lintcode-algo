# http://www.lintcode.com/zh-cn/problem/longest-words/


def longestWords(dictionary):
    """
    :param dictionary: a list of strings
    :return: a list of strings
    """
    res = []
    max_length = 0

    if dictionary == []:
        return res

    for word in dictionary:
        length = len(word)

        if length == max_length:
            res.append(word)

        if length > max_length:
            res = []
            res.append(word)
            max_length = length

    return res

dic = ["dog","google","facebook","internationalization","blabla"]
print(longestWords(dic))