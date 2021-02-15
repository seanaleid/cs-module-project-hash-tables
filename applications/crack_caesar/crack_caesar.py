# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# U --> find the frequency of each letter in the text and then decode the text 
# P --> 
    # 1. read text, split on space, and store in a list
    # 2. strip punctuation
    # 3. split letters
    # 4. check frequency and store in a cache

# with open('ciphertext.txt') as f:
#     cipher = f.read().split()

# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for key in range(len(letters)):
#     translated = ''
#     for symbol in cipher:
#         if symbol in letters:
#             num = letters.find(symbol)
#             num = num-key
#             if num < 0:
#                 num = num - len(letters)
#             translated = translated + letters[num]
#         else:
#             translated = translated + symbol
# print('Hacking key #%s: %s' % (key, translated))


def caesar():
    ignore = ' , . " : ; _ - ! ? ( ) 1 2 3 4 5 6 7 8 9 0 '
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_char = []
    cipher_dict = {}
    ord_alpha = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    with open('ciphertext.txt') as f:
        # ciper value has the original cipher text with punctuation and split on the spaces
        cipher = f.read().split()
    
    no_punc = [word.strip(ignore) for word in cipher]

    for word in no_punc:
        for char in word:
            if char in alpha:
                list_char.append(char)
    
    char_len = len(list_char)
    
    for letter in list_char:
        cipher_dict[letter] = list_char.count(letter)/char_len*100
    
    sort_dict = sorted(cipher_dict.items(), key=lambda pair: pair[1], reverse=True)

    decode = {}

    for i in range(len(ord_alpha)):
        decode[sort_dict[i]] = ord_alpha[i]
    
    new_dict = {}
    for item in decode.items():
        new_dict[item[0][0]] = item[1]
        
    # print(new_dict)
    deciphered = []
    for word in no_punc:
        for char in word:
            if char in ignore:
                deciphered.append(char)
            elif char in new_dict:
                deciphered.append(new_dict[char]) 
    print(" ".join(deciphered))

print(caesar())