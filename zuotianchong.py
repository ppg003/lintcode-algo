def leftPad(originalStr, size, padChar=' '):
    """
    :param originalStr: originalStr the string we want to append to
    :param size: size the target length of the string
    :param padChar: padChar the character to pad to the left side of the string
    :return: a string
    """
    length = len(originalStr)
    if length >= size:
        return originalStr

    res = padChar * (size - length) + originalStr
    return res