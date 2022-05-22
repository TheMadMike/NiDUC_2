from src.frame import Frame


def get_parity(frame: Frame):
    ones = 0
    for i in range(0, frame.size):
        if (frame.data >> i) & 1:
            ones += 1
            
    return int(ones % 2 != 0)