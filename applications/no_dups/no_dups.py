def no_dups(s):
    # Your code here
    # split the string
    # iterate over the string and check for words
    # first instance, put into a dictionary
        # .join()
        # 'word1 ', 'word2 ', 'word3 ' --> removes the spaces after the words
        # " ".join() --> list comprehension 
    newStr = s.split(' ')
    newArr = []
    for word in newStr:
        if word in newArr:
            pass
        elif newStr.count(word) >= 1:
            newArr.append(word)
    finalStr = ' '.join([str(el) for el in newArr])
    return finalStr


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))