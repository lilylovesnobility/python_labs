def format_record(rec):                                     #1
    if type(rec) is not tuple or len(rec) != 3:
        raise ValueError('Ожидается кортеж из 3 элементов')
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    if type(gpa) not in (int, float):
        raise TypeError('GPA введён неверно')
    if type(fio) is not str or len(fio.strip()) == 0:
        raise ValueError('ФИО введены неверно')
    if type(group) is not str or len(group.strip()) == 0:
        raise ValueError('Группа введена неверно')
    group = group.strip()
    parts = fio.strip().split()
    if len(parts) < 2:
        raise ValueError('ФИО должно содержать минимум фамилию и имя')
    surname = parts[0].capitalize()
    initials = ''
    for name in parts[1:3]:
        initials += name[0].upper() + '.'
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'
