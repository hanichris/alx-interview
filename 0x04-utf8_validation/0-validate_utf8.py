#!/usr/bin/python3
"""UTF-8 Validation."""


def validUTF8(data):
    """Determine if a given data set is a valid UtF-8 encoding.

    Args:
        data (List[int]): list of integers representing characters.
    Return:
        boolean: True if the data set is valid, else False.
    """
    # No. of bytes in the current UTF-8 character.
    n_bytes = 0

    # mask to check if MSB is set or not.
    mask1 = 1 << 7

    # mask to check if next MSB is set or not.
    mask2 = 1 << 6

    for num in data:
        # Get the number of set MSBs in the byte if this is the start.
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If in the middle processing part of a UTF-8 character.
            # Check the first two bits.
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
