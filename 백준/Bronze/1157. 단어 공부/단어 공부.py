from collections import defaultdict
word = str(input()).upper()
word_dict = defaultdict(int)

for letter in word:
    word_dict[letter] += 1

min_count = -1
cnt = 0
idx = 0
for num in word_dict.values():
    if num > min_count:
        min_count = num
        idx = list(word_dict.values()).index(num)
        cnt = 0
    elif num == min_count:
        cnt += 1
if cnt > 0:
    print('?')
else:
    print(list(word_dict.keys())[idx])