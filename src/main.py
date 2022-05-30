from sender import Sender
from parity import get_parity, ascii_to_frames_with_parity
from doubling import ascii_to_frames_with_doubling, check_doubling
from utils import frames_to_ascii, print_transmission_correctness
from errors import generate_low_noise
from crc32 import string_to_crc32_frames, check_crc32_frame

sender = Sender(check_crc32_frame)
#sender.set_noise_function(generate_low_noise_for_string)

### SENDING FRAMES
stringToSend = "Hello, world!"
print(f"Sending string: {stringToSend}")

sender.send_frames(string_to_crc32_frames(stringToSend))

### PRINTING RECEIVED FRAMES

receivedString = frames_to_ascii(sender.receiver.framesReceived)
print(f"Received string: {receivedString}")

print_transmission_correctness(stringToSend, receivedString)

print(f"Transmisssions in total: {sender.transmissionsTotal}")
print(f"Error rate: {(1.0 - len(stringToSend) / sender.transmissionsTotal) * 100.0 : 0.2f}%")
