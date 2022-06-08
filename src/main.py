from komm import BinarySymmetricChannel
from crc32 import generate_lookup_table
from gilbert import gilbert_elliot_channel

from tests import test_crc32, test_doubling, test_parity_bit

string_to_send = "Hi!"
bsc = BinarySymmetricChannel(0.1)
gec = gilbert_elliot_channel(0.1, 0.1, 1.0)

POLYNOMIAL = 0xEDB88320
CRCLookupTable = []
generate_lookup_table(POLYNOMIAL, CRCLookupTable)

channel = bsc

test_parity_bit(string_to_send, channel, 1000)

test_doubling(string_to_send, channel, 1000)

test_crc32(string_to_send, channel, 1000, CRCLookupTable)