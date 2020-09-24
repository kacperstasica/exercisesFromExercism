class Matrix:
    def __init__(self, matrix_string):
        '''
        Object instance is already converted
        from list of strings e.g. "1 2 3\n4 5 6"
        into list of list of integers [[1,2,3], [4,5,6]]
        in such case.
        '''
        row_strings = [row.split() for row in matrix_string.split('\n')]
        row_ints = [[int(num) for num in row] for row in row_strings]
        self.matrix_string = row_ints

    def row(self, index):
        return self.matrix_string[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix_string]
