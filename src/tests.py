from parity import append_parity_bit, parity
from crc32 import append_crc32, check_crc32
from utility import bits_to_bytes, string_to_byte_list, byte_list_to_string, bytes_to_bits, get_bit_error
from copy import deepcopy

### Parity bit test ###
def test_parity_bit(bit_list: list, channel, retries):
    detected = 0
    undetected = 0
    falseErrors = 0
    total = 0
    bit_errors = 0
    bits_sent = 0

    for i in range(0, retries):
        sent = deepcopy(bit_list)
        append_parity_bit(sent)
        bits_sent += len(sent)
        receieved = channel(sent)

        bit_errors += get_bit_error(sent, receieved)
        if get_bit_error(sent, receieved) != 0:
            total += 1
            if parity(receieved):
                detected += 1
            else:
                undetected += 1

        elif parity(receieved):
            falseErrors += 1

    print("Method: parity bit")
    print(f"Undetected: {undetected} / Detected: {detected} / False positives: {falseErrors}")
    print(f"Frames with errors in total: {total}")
    bit_error_rate = bit_errors / bits_sent
    print(f"Bit error rate: {bit_error_rate :.4f}")


def check_doubling(bit_list: list):
    for i in range(0, len(bit_list) // 2):
        if bit_list[i] != bit_list[(len(bit_list) // 2 + i)]:
            return False
        
    return True


### Doubling test ###
def test_doubling(bit_list: list, channel, retries):
    detected = 0
    undetected = 0
    falseErrors = 0
    total = 0
    bit_errors = 0
    bits_sent = 0

    for i in range(0, retries):
        sent = deepcopy(bit_list)
        sent = [*sent, *sent]
        bits_sent += len(sent)
        receieved = channel(sent)

        bit_errors += get_bit_error(sent, receieved)
        if get_bit_error(sent, receieved) != 0:
            total += 1
            if not check_doubling(receieved):
                detected += 1
            else:
                undetected += 1

        elif parity(receieved):
            falseErrors += 1

    print("Method: doubling")
    print(f"Undetected: {undetected} / Detected: {detected} / False positives: {falseErrors}")
    print(f"Frames with errors in total: {total}")
    bit_error_rate = bit_errors / bits_sent
    print(f"Bit error rate: {bit_error_rate :.4f}")

### CRC32 test ###
def test_crc32(bit_list: list, channel, retries, CRCLookupTable: list):
    detected = 0
    undetected = 0
    falseErrors = 0
    total = 0
    bit_errors = 0
    bits_sent = 0

    for i in range(0, retries):
        sent = deepcopy(bit_list)
        append_crc32(sent, CRCLookupTable)
        bits_sent += len(sent)
        receieved = channel(sent)

        bit_errors += get_bit_error(sent, receieved)
        if get_bit_error(sent, receieved) != 0:
            total += 1
            if not check_crc32(receieved, CRCLookupTable):
                detected += 1
            else:
                undetected += 1

        elif not check_crc32(receieved, CRCLookupTable):
            falseErrors += 1

    print("Method: CRC32")
    print(f"Undetected: {undetected} / Detected: {detected} / False positives: {falseErrors}")
    print(f"Frames with errors in total: {total}")
    bit_error_rate = bit_errors / bits_sent
    print(f"Bit error rate: {bit_error_rate :.4f}")