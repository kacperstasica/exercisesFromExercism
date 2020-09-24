def saddle_points(matrix):

    if not matrix:
        return []
    elif sum(len(i) for i in matrix) % len(matrix[0]) != 0:
        raise ValueError('Irregular matrix error.')

    point_list = []

    for idx, row in enumerate(matrix):
        for i in range(len(row)):
            col = [row[i] for row in matrix]

            if max(row) == min(col):
                point_list.append({'row': idx+1, 'column': i+1})
    return point_list
