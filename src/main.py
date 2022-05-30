from sender import Sender
from parity import get_parity
from utils import ascii_to_frames_with_parity, frames_to_ascii

sender = Sender(get_parity)

### SENDING FRAMES
stringToSend = "Hello, world!"
print(f"Sending string: {stringToSend}")

sender.send_frames(ascii_to_frames_with_parity(stringToSend))

### PRINTING RECEIVED FRAMES

print(f"Received string: {frames_to_ascii(sender.receiver.framesReceived)}")
