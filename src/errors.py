from frame import Frame
import random

def generate_bitflip(frame: Frame):
    frame.data ^= (1 << random.randint(0, frame.size))

def generate_random_frame_number(frame: Frame):
    frame.number = random.randint(0, 30)

def generate_low_noise(frame: Frame):
    flip = random.randint(0, 5)
    if flip == 0:
        generate_bitflip(frame)
        return
    
    flip = random.randint(0, 5)

    if flip == 0:
        generate_random_frame_number(frame)