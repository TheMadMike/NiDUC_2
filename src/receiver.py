from frame import Frame
from responses import Response

class Receiver:
    requestNumber: int = 0
    framesReceived = []

    def __init__(self, errorDetectionFunction):
        self.isErrorDetected = errorDetectionFunction


    def receive(self, frame: Frame):
        if self.isErrorDetected(frame) or self.requestNumber != frame.number:
            return Response.ERROR

        self.framesReceived.append(frame)
        self.requestNumber += 1
        return Response.ACK
