# Your code here

    # U --> print out each word followed by #(times the number of appearances that word makes in the text)
        # sort first by number of appearances and then alphabetically
    # P -->
        # 1. read file
        # 2. split text
        # 3. iterate over the list, count, and store in a cache
        # 4. loop over the keys in the dictionary, print the words and #*appearances in the console, sorted by amount and then alphabetically

def histo():
    ignore = ' " : ; , . - + = / \ | [ ] { } ( ) * ^ & ? ! '
    with open('robin.txt') as f:
        words = f.read().lower().split()
    clean_words = [el.strip(ignore) for el in words]
    word_dict = {}
    count = 0
    for i in clean_words:
        word_dict[i] = clean_words.count(i)
    sorted_words = sorted(word_dict.items(), key=lambda pair: pair[1], reverse=True)

    print("{:<10}{:<10}".format('WORD', 'AMOUNT'))
    for pair in sorted_words:
        new_pair_amount = f"                {'#'*pair[1]}" 
        print("{:<10}{:<10}".format(pair[0], new_pair_amount))

    # for pair in sorted_words:
    #     print(pair[0], f"       {'#'*pair[1]}")

print(histo())