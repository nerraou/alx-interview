#!/usr/bin/python3
"""
utf8 validation
"""


def is_valid(c):
    """
    check single value
    """
    if c <= 0x7F:
        return True
    if 0xC080 == c:
        return True

    if 0xC280 <= c and c <= 0xDFBF:
        return (c & 0xE0C0) == 0xC080

    if 0xEDA080 <= c and c <= 0xEDBFBF:
        return False

    if 0xE0A080 <= c and c <= 0xEFBFBF:
        return ((c & 0xF0C0C0) == 0xE08080)

    if 0xF0908080 <= c and c <= 0xF48FBFBF:
        return (c & 0xF8C0C0C0) == 0xF0808080

    return False


def validUTF8(data):
    """
    check all list contains valid utf8
    """

    for c in data:
        if not is_valid(c):
            return False
    return True
