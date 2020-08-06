import random
import json 
# Read in all the words in one go
# Store them to a variable 
with open("input.txt") as f:
    words = f.read()

# the text is STORED in variable that we can read in the terminal
# print(words)

# SPLIT the data into keys 
corpus = words.split()
# prints a list of words
# print(corpus)
# CREATE pairs to keys
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield(corpus[i], corpus[i+1])
pairs = make_pairs(corpus)

# TODO: analyze which words can follow other words
# Your code here

# APPEND to a dictionary
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

def five_sentences():
    first_word = random.choice(corpus)
    markov = ' '
    

    while first_word.islower():
        first_word = random.choice(corpus)

        chain = [first_word]

        n_words = 100

        for i in range(n_words):
            chain.append(random.choice(word_dict[chain[-1]]))
    return markov.join(chain)

print(five_sentences())
# TODO: construct 5 random sentences
# Your code here

# SHOW the dictionary of keys and tokens (values, list of words that can follow the keys)
# print(word_dict)
# OPTION 1 to print a dictionary 
# need json.dumps(dictionary name, indent=amount of spaces, sort_keys=alphabetically, throws an error if a mix of nums and strs)
# print(json.dumps(word_dict, indent=4, sort_keys=True))


# def five_sentences():
#     first_word = random.choice(corpus)
#     markov = ' '
#     end = ' . ? ! '
#     count = 0

#     while first_word.islower() and count < 5:
#         chain = [first_word]
#         chain.append(random.choice(word_dict[chain[-1]]))
#         count+=1
        # first_word = random.choice(corpus)

        # chain = [first_word]

        # n_words = 100

        # for i in range(n_words):
        #     chain.append(random.choice(word_dict[chain[-1]]))
    # return markov.join(chain)
    # return chain



