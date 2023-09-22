#Program that reads a text file and performs various analyses on its content

import re

name = input('Enter file (enter for default text): ')
if len(name) < 1:
    name = 'words.txt'
handle = open(name)

di = dict()

countMax = None
wordMax = None

x = input('Dif between mayus and minus? y/n: ')

# Initialize variables for word count, sentence count, and paragraph count
word_count = 0
sentence_count = 0
paragraph_count = 1

for line in handle:
    if x.lower() == 'n':
        line = line.lower()

    # Split the line into sentences using regular expressions
    sentences = re.split(r'[.!?]', line)
    #print(sentences)

    for sentence in sentences:
        # Count sentences
        if sentence.strip():
            sentence_count += 1

            # Split each sentence into words
            words = sentence.split()
            word_count += len(words)

            for word in words:
                # Count words
                di[word] = di.get(word, 0) + 1

    # Count paragraphs
    if not line.strip():
        paragraph_count += 1

# Calculate average word length
total_word_length = sum(len(word) for word in di)
average_word_length = round(total_word_length / word_count if word_count > 0 else 0,2)

# Find the most common word
for k, v in di.items():
    if countMax is None or v > countMax:
        wordMax = k
        countMax = v

print('Number of words:',word_count)
print('Number of sentences:',sentence_count)
print('Number of paragraphs:',paragraph_count)
print('Average word length:',average_word_length)
print('Most common word: ' + str(wordMax) + ' (Frequency: ' + str(countMax) + ')' )
