word = input('enter the word ')
char_dict = {}
for char in set(word):
    char_dict[char] = word.count(char)

print(char_dict)