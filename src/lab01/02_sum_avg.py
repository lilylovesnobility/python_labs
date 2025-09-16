a = input("a: ").replace(",", ".")
b = input("b: ").replace(",", ".")
a, b = float(a), float(b)
s = a + b
avg = s / 2
print(f"sum={s:.2f}; avg={avg:.2f}")
