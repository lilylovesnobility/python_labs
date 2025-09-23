fio = input("ФИО: ")
fio_stripped = fio.strip()
parts = fio_stripped.split()
initials = "".join([p[0].upper() for p in parts]) + "."
print(f"Инициалы: {initials}")
print(f"Длина (символов): {len(fio_stripped.replace(' ', ''))}")
