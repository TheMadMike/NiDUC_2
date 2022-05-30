from receiver import Receiver
from frame import Frame
from responses import Response
from logger import print_debug

class Sender:
    receiver: Receiver
    frameNumber: int
    frames = []
    retransmissionLimit = 10
    retransmissionCount = 0
    transmissionsTotal = 0
    generateNoise = None

    def __init__(self, errorDetectionFunction):
        self.receiver = Receiver(errorDetectionFunction)

    def set_noise_function(self, noiseGenerator):
        self.generateNoise = noiseGenerator

    def send_frames(self, frames):
        if len(frames) < 1:
            return
        
        self.frames = frames
        self.frameNumber = 0

        self.send_frame(frames[0])


    def send_frame(self, frame: Frame):
        print_debug(f"SENDING: No: {self.frameNumber} Data: {hex(frame.data)}")

        frameToSend = frame.copy()
        if self.generateNoise is not None:
            self.generateNoise(frameToSend)

        self.transmissionsTotal += 1
        response = self.receiver.receive(frameToSend)
        if response == Response.ACK:
            print_debug("ACK")
            self.frameNumber += 1
            self.retransmissionCount = 0
        else:
            print_debug("NACK")
            self.retransmissionCount += 1

        if self.frameNumber >= len(self.frames) or self.retransmissionCount >= self.retransmissionLimit:
            print_debug("TRANSMISSION ENDED")
            return

        self.send_frame(self.frames[self.frameNumber])
        
    
