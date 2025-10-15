text = "hello world"
char_count = {}

for char in text:
    if char in char_count and char!='':
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
########################
# from collections import Counter

# text = "hello world"
# counter = Counter(text)

# print(counter)


# ########################

# text = "Hello World".replace(" ", "").lower()
# counter = Counter(text)
# print(counter)
