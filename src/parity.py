def get_parity(frame, size):
    ones = 0
    for i in range(0, size):
        if (frame >> i) & 1:
            ones += 1
            
    return int(ones % 2 != 0)