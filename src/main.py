from komm import BinarySymmetricChannel
from crc32 import generate_lookup_table
from gilbert import gilbert_elliot_channel

from tests import test_crc32, test_doubling, test_parity_bit

POLYNOMIAL = 0b1
CRCLookupTable = []
generate_lookup_table(POLYNOMIAL, CRCLookupTable)

data_to_send = [0, 1, 0, 0]

def perform_tests(repetitions, channel):
    test_parity_bit(data_to_send, channel, 1000)
    test_doubling(data_to_send, channel, 1000)
    test_crc32(data_to_send, channel, 1000, CRCLookupTable)

bsc = BinarySymmetricChannel(0.99)
gec = gilbert_elliot_channel(0.1, 0.1, 1.0)

print ("Repetitions: 1000, Channel: BSC")
perform_tests(1000, bsc)

print ("Repetitions: 1000, Channel: Gilbert-Elliot")
perform_tests(1000, gec)

