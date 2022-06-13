def parity(data: list):
    ones = 0
    for bit in data:
        ones += bit
            
    return int(ones % 2 != 0)

def append_parity_bit(data: list):
    data.append(parity(data))