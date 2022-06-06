from komm import BinarySymmetricChannel
from parity import append_parity_bit, parity
from utility import bits_to_bytes, string_to_byte_list, byte_list_to_string, bytes_to_bits

def test_parity_bit(string: str, channel, retries):
    detected = 0
    undetected = 0

    for i in range(0, retries):
        sent = string_to_byte_list(string)
        append_parity_bit(sent, len(sent))
        receieved = channel(bytes_to_bits(sent))

        receieved_str = byte_list_to_string(bits_to_bytes(receieved))
        receieved_str = receieved_str[0:len(receieved_str) - 1]

        if string != receieved_str:
            receieved_bytes = bits_to_bytes(receieved)
            if parity(receieved_bytes, len(receieved_bytes)):
                detected += 1
            else:
                undetected += 1

    print(f"Undetected: {undetected} / Detected: {detected}")

### Parity bit ###
string_to_send = "Hello, world! \n"
bsc = BinarySymmetricChannel(0.1)

test_parity_bit(string_to_send, bsc, 100)

### Doubling ###



### CRC32 ###