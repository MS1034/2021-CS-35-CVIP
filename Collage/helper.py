from itertools import product


def grid(i, height, width):
    r, c = (2 if i > 2 else 1, i//2 if i % 2 == 0 and i != 2 else i//2+1)
    arr_h = [height // r] * r
    arr_w = [width // c] * c

    if i % 2 == 0:
        arr_h[0] = height // r + height % r
        arr_w[0] = width // c + width % c

    tuples = []
    h_start = 0
    for h_end in arr_h:
        w_start = 0
        for w_end in arr_w:
            tuples.append(((h_start, h_start + h_end),
                          (w_start, w_start + w_end)))
            w_start += w_end
        h_start += h_end

    return tuples


# Example usage:
i = 5
height = 1000
width = 1500
result = grid(i, height, width)
print(type(result))
print(result)
