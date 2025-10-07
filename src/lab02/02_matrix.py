def transpose(mat):                                         #1
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError('Строки разной длины')
    result = []
    for j in range(cols):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result

def row_sums(mat):                                          #2
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError('Строки разной длины')
    sums = []
    for row in mat:
        total = 0
        for x in row:
            total += x
        sums.append(total)
    return sums

def col_sums(mat):                                          #3
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError('Строки разной длины')
    sums = [0] * cols
    for row in mat:
        for j in range(cols):
            sums[j] += row[j]
    return sums
