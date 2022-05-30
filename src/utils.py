from frame import Frame
from parity import get_parity

def ascii_to_frames_with_parity(string: str):
    frames = []
    for i in range(0, len(string)):
        frame = Frame(i, 0, 9)
        frame.data = ord(string[i])
        frame.data |= (get_parity(frame) << 8)
        frames.append(frame)
    
    return frames

def frames_to_ascii(frames: list):
    s = ""
    for frame in frames:
        s += chr(frame.data & 0xFF)
    
    return s