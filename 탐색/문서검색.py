import sys

sentence = input()
word = input()

# ababababa 9
# aba 3
cnt = 0
index = 0

while len(sentence) - index >= len(word):
    if sentence[index:index+len(word)] == word:
        cnt += 1
        index += len(word)
    else:
        index += 1

print(cnt)
