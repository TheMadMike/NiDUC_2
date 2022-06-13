from numpy import append
from utility import bits_to_bytes

def generate_lookup_table(polynomial: int, table: list):
    remainder = 0
    for b in range(0, 256):
        remainder = b
        for i in range(0, 8):
            if remainder & 1:
                remainder = (remainder >> 1) ^ polynomial
            else:
                remainder = (remainder >> 1)
        
        table.append(remainder)

def crc32(data: list, CRCTable: list):
    crc32 = 0xFFFFFFFF

    for i in range(0, len(data)):
        lookupIndex = (crc32 ^ (data[i] & 0xff)) & 0xff
        crc32 = (crc32 >> 8) ^ CRCTable[lookupIndex]

    crc32 ^= 0xFFFFFFFF
    return crc32

def append_crc32(data: list, CRCTable: list):
    checksum = crc32(bits_to_bytes(data), CRCTable)
    for i in range(0, 32):
        data.append((checksum >> (31 - i)) & 1)

def check_crc32(data: list, CRCTable: list):
    checksum = 0
    for i in range(0, 32):
        checksum |= data[len(data) -1 - i] << i

    return checksum == crc32(bits_to_bytes(data[0:len(data) - 32]), CRCTable)


lookup = []
generate_lookup_table(0b010, lookup)
data = [0, 1, 1, 0, 1]
append_crc32(data, lookup)
check_crc32(data, lookup)