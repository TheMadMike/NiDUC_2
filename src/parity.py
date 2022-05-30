from frame import Frame

def get_parity(frame: Frame):
    ones = 0
    for i in range(0, frame.size):
        if (frame.data >> i) & 1:
            ones += 1
            
    return int(ones % 2 != 0)

def ascii_to_frames_with_parity(string: str):
    frames = []
    for i in range(0, len(string)):
        frame = Frame(i, 0, 9)
        frame.data = ord(string[i])
        frame.data |= (get_parity(frame) << 8)
        frames.append(frame)
    
    return frames