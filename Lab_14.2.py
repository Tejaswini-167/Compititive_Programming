# 14.2
text = input()

pattern = input()

count = 0

for i in range(len(text)):

    if text.startswith(pattern, i):
        count += 1

print(count)