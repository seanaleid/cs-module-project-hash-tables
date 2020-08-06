
def word_count(s):
    char_list = ' " : ; , . - + = / \ | [ ] { } ( ) * ^ & '
    
    newStr = s.lower().split()
    # refactored for a list comprehension
    newArr = [el.strip(char_list) for el in newStr]

    # OLD WAY - for loop
    # newArr = []
    # for el in newStr:
    #     newArr.append(el.strip(char_list))
    
    if s == "" or newArr == [""]:
        return {}
    else:
        cache = {}
        for el in newArr:
            cache[el] = newArr.count(el)
        return cache
    

# print(word_count(""))
# print(word_count("Hello"))
# print(word_count("Hello    hello"))
# print(word_count('This is a test of the  Emergency  Broadcast  Network. This is only a test.'))


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
