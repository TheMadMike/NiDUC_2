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
    checksum = crc32(data, CRCTable)
    for i in range(0, 4):
        data.append((checksum >> (3-i)*8) & 0xFF)

def check_crc32(data: list, CRCTable: list):
    checksum = 0
    for i in range(0, 4):
        checksum |= data[len(data) - 1 - i] << (i*8)

    return checksum == crc32(data[0:len(data) - 4], CRCTable)
    