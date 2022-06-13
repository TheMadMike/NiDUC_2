def string_to_byte_list(string: str):
    byte_list = []
    for c in string:
        byte_list.append(ord(c))
    
    return byte_list


def byte_list_to_string(byte_list: list):
    string = ""
    for c in byte_list:
        string += chr(c)
    
    return string

def bytes_to_bits(byte_list: list):
    bit_list = []
    for i in range(0, len(byte_list)*8):
        bit_list.append(byte_list[i // 8] >> (7 - (i % 8)) & 1)

    return bit_list

def bits_to_bytes(bit_list: list):
    byte_list = []
    byte_list.append(0)
    for i in range(0, len(bit_list) // 8):
        byte_list.append(0)

    x = 0
    for bit in bit_list:
        byte_list[x // 8] |= (bit << (7 - (x % 8))) 

        x += 1

    return byte_list

def get_bit_error(a: list, b: list):
    error = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            error += 1
    
    return error