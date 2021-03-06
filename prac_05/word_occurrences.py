"""
Write a program to count the occurrences of words in a string. The program should ask the user for a string,
then print the counts of how many of each word are in the file.
"""

string_to_count = (input("Text: ")).lower().split(" ")
counted_words = {}
for word in string_to_count:
    counted_words[word] = counted_words.get(word, 0) + 1
max_word_len = max(len(word) for word in counted_words)

counted_words_sorted = list(counted_words.items())
counted_words_sorted.sort()

for word, counted_occurrence in counted_words_sorted:
    print("{:{}} : {}".format(word, max_word_len, counted_occurrence))
