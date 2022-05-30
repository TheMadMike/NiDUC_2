from sender import Sender
from parity import get_parity, ascii_to_frames_with_parity
from doubling import ascii_to_frames_with_doubling, check_doubling
from utils import frames_to_ascii, print_transmission_correctness
from errors import generate_low_noise

sender = Sender(check_doubling)
sender.set_noise_function(generate_low_noise)

### SENDING FRAMES
stringToSend = "Hello, world!"
print(f"Sending string: {stringToSend}")

sender.send_frames(ascii_to_frames_with_doubling(stringToSend))

### PRINTING RECEIVED FRAMES

receivedString = frames_to_ascii(sender.receiver.framesReceived)
print(f"Received string: {receivedString}")

print_transmission_correctness(stringToSend, receivedString)

print(f"Transmisssions in total: {sender.transmissionsTotal}")
print(f"Error rate: {(1.0 - len(stringToSend) / sender.transmissionsTotal) * 100.0 : 0.2f}%")
