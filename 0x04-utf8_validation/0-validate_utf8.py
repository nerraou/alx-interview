#!/usr/bin/python3
"""
utf8 validation
"""


def validUTF8(data):
    """
    check all list contains valid utf8
    """
    remaining_bytes = 0

    for byte in data:
        byte = 255 & byte
        if remaining_bytes == 0:
            if byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
