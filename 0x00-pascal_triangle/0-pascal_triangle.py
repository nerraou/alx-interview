def pascal_triangle(n):
    """generate pascal triangle"""
    if (n <= 0):
        return []

    matrix = [[1]]

    for i in range(1, n):
        matrix.append([])

        for j in range(0, i + 1):
            if (j == 0 or j == i):
                matrix[i].append(1)
            else:
                a = matrix[i - 1][j - 1]
                b = matrix[i - 1][j]
                matrix[i].append(a + b)

    return matrix
