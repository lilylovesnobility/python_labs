from lib.text import normalize, tokenize, count_freq, top_n                         #1
text = input()
text = normalize(text)
tokens = tokenize(text)
freq = count_freq(tokens)
top = top_n(freq, 5)
print("Всего слов:", len(tokens))
print("Уникальных слов:", len(freq))
print("Топ-5:")
for word, count in top:
    print(f"{word}:{count}")
