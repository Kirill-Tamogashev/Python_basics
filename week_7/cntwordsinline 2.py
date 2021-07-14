fin = open('input.txt', 'r')

words = fin.read().split()
word_dict = dict()
num_arr = []
for word in words:
    if word in word_dict:
        word_dict[word] += 1
        num_arr.append(word_dict[word])
    else:
        word_dict[word] = 0
        num_arr.append(word_dict[word])
print(*num_arr)
fin.close()
