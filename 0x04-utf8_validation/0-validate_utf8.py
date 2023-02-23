#!/usr/bin/python3
'''A script for validating UTF8.
'''

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
    data: A list of integers representing 1 byte of data each.
    
    Returns:
    True if data is a valid UTF-8 encoding, else returns False.
    """
    # Counter for number of bytes in current UTF-8 character
    bytes_left = 0
    
    # Loop through the data list
    for byte in data:
        # If this is the start of a new UTF-8 character
        if bytes_left == 0:
            # Count the number of bytes in the character
            if byte >> 7 == 0b0:
                # 1 byte character
                bytes_left = 0
            elif byte >> 5 == 0b110:
                # 2 byte character
                bytes_left = 1
            elif byte >> 4 == 0b1110:
                # 3 byte character
                bytes_left = 2
            elif byte >> 3 == 0b11110:
                # 4 byte character
                bytes_left = 3
            else:
                # Invalid UTF-8 character start byte
                return False
        else:
            # This byte should be a continuation byte
            if byte >> 6 != 0b10:
                return False
            bytes_left -= 1
    # If we reach the end of the loop and there are bytes left over
    if bytes_left != 0:
        return False
    return True
