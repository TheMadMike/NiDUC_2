from frame import Frame

def frames_to_ascii(frames: list):
    s = ""
    for frame in frames:
        s += chr(frame.data & 0xFF)
    
    return s

def print_transmission_correctness(sent: str, received: str):

    correctFrames = 0
    totalFrames = len(sent)

    for i in range(0, len(received)):
        if sent[i] == received[i]:
            correctFrames += 1

    print(f"Frames transmitted (correctly/total): {correctFrames} / {totalFrames} ({correctFrames / totalFrames * 100.0 : .2f}% )")