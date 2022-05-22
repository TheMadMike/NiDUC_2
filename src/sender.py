from receiver import Receiver
from frame import Frame
from responses import Response

class Sender:
    receiver: Receiver
    frameNumber: int
    frames = []
    retransmissionLimit = 10
    retransmissionCount = 0

    def __init__(self, errorDetectionFunction):
        self.receiver = Receiver(errorDetectionFunction)


    def send_frames(self, frames):
        if len(frames) < 1:
            return
        
        self.frames = frames
        self.frameNumber = 0

        self.send_frame(frames[0])


    def send_frame(self, frame: Frame):

        response = self.receiver.receive(frame)
        if response == Response.ACK:
            self.frameNumber += 1
            self.retransmissionCount = 0
        else:
            self.retransmissionCount += 1

        if self.frameNumber >= len(self.frames) or self.retransmissionCount >= self.retransmissionLimit:
            return

        self.send_frame(self.frames[self.frameNumber])
        
    
