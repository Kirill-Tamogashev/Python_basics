fin = open('input.txt', 'r')

words = fin.read().split()
fin.close()
word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 0
for key in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
    print(key[0])
