from collections import defaultdict

# Creates a default value of 0 for new keys
word_count = defaultdict(int)

# List of words we will count
words = [
'apple', 'banana', 'apple',
'mango', 'apple'
]

# Count the frequency of words in a list
for word in words:
	word_count[word] += 1

print(word_count)