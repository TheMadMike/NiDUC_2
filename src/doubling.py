from frame import Frame

def check_doubling(frame: Frame):
    if frame.size % 2 != 0:
        raise "Error frame size not divisible by 2 (required for doubling)"
    m = frame.size // 2
    
    return (frame.data >> m) != (frame.data & ((1 << m) - 1))


def ascii_to_frames_with_doubling(string: str):
    frames = []
    for i in range(0, len(string)):
        frame = Frame(i, 0, 16)
        frame.data = ord(string[i])
        frame.data |= (frame.data << 8)
        frames.append(frame)
    
    return frames