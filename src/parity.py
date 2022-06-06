def parity(data: list, size: int):
    ones = 0
    for i in range(0, size * 8):
        if (data[i // 8] >> (i % 8) ) & 1:
            ones += 1
            
    return int(ones % 2 != 0)

def append_parity_bit(data: list, size: int):
    data.append(parity(data, size))