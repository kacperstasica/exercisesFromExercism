def slices(series, length):
    sliced_serie = []
    if len(series) <= 0:
        raise ValueError('Error. The series has no length.')
    if length <= 0:
        raise ValueError('Error. Slice length cannot be zero or negative.')
    if len(series) < length:
        raise ValueError('Error. Slice length is too large.')
    for i in range(len(series)):
        x = series[i:length + i]
        if len(x) == length:
            sliced_serie.append(series[i:length + i])
    return sliced_serie
