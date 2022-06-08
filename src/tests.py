from parity import append_parity_bit, parity
from crc32 import append_crc32, check_crc32
from utility import bits_to_bytes, string_to_byte_list, byte_list_to_string, bytes_to_bits, get_bit_error

### Parity bit test ###
def test_parity_bit(string: str, channel, retries):
    detected = 0
    undetected = 0
    falseErrors = 0
    total = 0
    bit_errors = 0
    bits_sent = 0

    for i in range(0, retries):
        sent = string_to_byte_list(string)
        append_parity_bit(sent, len(sent))
        bits_sent += len(sent)*8
        receieved = channel(bytes_to_bits(sent))

        receieved_str = byte_list_to_string(bits_to_bytes(receieved))
        receieved_str = receieved_str[0:len(receieved_str) - 1]
        receieved_bytes = bits_to_bytes(receieved)

        bit_errors += get_bit_error(bytes_to_bits(sent), receieved)
        if get_bit_error(bytes_to_bits(sent), receieved) != 0:
            total += 1
            if parity(receieved_bytes, len(receieved_bytes)):
                detected += 1
            else:
                undetected += 1

        elif parity(receieved_bytes, len(receieved_bytes)):
            falseErrors += 1

    print("Method: parity bit")
    print(f"Undetected: {undetected} / Detected: {detected} / False errors: {falseErrors}")
    print(f"Frames with errors in total: {total}")
    bit_error_rate = bit_errors / bits_sent
    print(f"Bit error rate: {bit_error_rate :.4f}")


### Doubling test ###
def test_doubling(string: str, channel, retries):
    detected = 0
    undetected = 0
    falseErrors = 0
    total = 0
    bit_errors = 0
    bits_sent = 0

    for i in range(0, retries):
        sent = string_to_byte_list(string)
        sent = [*sent, *sent]
        bits_sent += len(sent)*8
        receieved = channel(bytes_to_bits(sent))

        receieved_str = byte_list_to_string(bits_to_bytes(receieved))
        receieved_str = receieved_str[0:(len(receieved_str)//2)]
        receieved_bytes = bits_to_bytes(receieved)

        bit_errors += get_bit_error(bytes_to_bits(sent), receieved)
        if get_bit_error(bytes_to_bits(sent), receieved) != 0:
            total += 1
            if receieved_bytes[0:(len(receieved_str)//2)] != receieved_bytes[(len(receieved_str)//2):len(receieved_bytes)]:
                detected += 1
            else:
                undetected += 1

        elif parity(receieved_bytes, len(receieved_bytes)):
            falseErrors += 1

    print("Method: doubling")
    print(f"Undetected: {undetected} / Detected: {detected} / False errors: {falseErrors}")
    print(f"Frames with errors in total: {total}")
    bit_error_rate = bit_errors / bits_sent
    print(f"Bit error rate: {bit_error_rate :.4f}")

### CRC32 test ###
def test_crc32(string: str, channel, retries, CRCLookupTable: list):
    detected = 0
    undetected = 0
    falseErrors = 0
    total = 0
    bit_errors = 0
    bits_sent = 0

    for i in range(0, retries):
        sent = string_to_byte_list(string)
        append_crc32(sent, CRCLookupTable)
        bits_sent += len(sent)*8
        receieved = channel(bytes_to_bits(sent))

        receieved_str = byte_list_to_string(bits_to_bytes(receieved))
        receieved_str = receieved_str[0:len(receieved_str) - 4]
        receieved_bytes = bits_to_bytes(receieved)

        bit_errors += get_bit_error(bytes_to_bits(sent), receieved)
        if get_bit_error(bytes_to_bits(sent), receieved) != 0:
            total += 1
            if not check_crc32(receieved_bytes, CRCLookupTable):
                detected += 1
            else:
                undetected += 1

        elif not check_crc32(receieved_bytes, CRCLookupTable):
            falseErrors += 1

    print("Method: CRC32")
    print(f"Undetected: {undetected} / Detected: {detected} / False errors: {falseErrors}")
    print(f"Frames with errors in total: {total}")
    bit_error_rate = bit_errors / bits_sent
    print(f"Bit error rate: {bit_error_rate :.4f}")