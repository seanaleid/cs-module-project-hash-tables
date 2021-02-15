import random

# UPER
    # Understand 
    # Plan
        # 1. Read the file `input.txt` and split it into words.
            # Already read in
            # Split into words
        # 2. Analyze the text, building up the dataset of which words can follow a word.
            # Which words can follow a word? any word that actually follows a word
                # any word at index + 1
            # How can we build the data set?
                # Use a hashtable 
                    # good way to realate one piece of info, with other info, relational
                    # frequent lookups
                    # Key: word, value list of all hte words that cna follow this word
        # 3. Choose a random "start word" to begin.
            # What is a "start word"?
                # starts with first or second character is a capitalized  
            # Make a list of start words
        # 4. Loop over, print choose a random following word, if it's a stop word, stop
            # Ends with a period, question mark, or exclamation mark or the second to last character is .?!
    # Execute 
    # Reflect 

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

# print(words)
# TODO: analyze which words can follow other words
dataset = {}

for i in range(len(words) -1):
    word = words[i]
    next_word = words[i+1]

    if word not in dataset:
        dataset[word] = [next_word]
    else:
        dataset[word].append(next_word)

# make a list of start words
# If the 1st or 2nd character is capitalized, put into a list
# Loop over words and put any start word into a list
# You can add a .keys() to your HashTable class
start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)



def five_sentences():
    word = random.choice(start_words)
    count = 0
    stop_signs = "?.!"
    while count < 5:
        count+=1
        stopped = False
        while not stopped:
            # print the word
            print(word, end=' ')
            
            # if it's a stop word, stop
            if word[-1] is stop_signs or len(word) > 1 and word[-2] in stop_signs:
                stopped = True
            
            # choose a random following word
            following_words = dataset[word]
            word = random.choice(following_words)
        

print(five_sentences())
# TODO: construct 5 random sentences
# Your code here

