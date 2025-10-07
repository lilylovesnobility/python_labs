def min_max(nums):                                          #1
    if len(nums) == 0:
        raise ValueError('Список пуст')
    return (min(nums), max(nums))

def unique_sorted(nums):                                    #2
    return sorted(set(nums))


def flatten(mat):                                           #3
    result = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError('Строка/элемент не является списком/кортежем')
        result.extend(row)
    return result


