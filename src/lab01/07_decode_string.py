s = input().strip()
start = next(i for i, ch in enumerate(s) if ch.isupper())
digit_index = next(i for i, ch in enumerate(s) if ch.isdigit() and i + 1 < len(s))
step = (digit_index + 1) - start

decoded = ""
for i in range(start, len(s), step):
    decoded += s[i]
    if s[i] == ".":
        break

print(decoded)
