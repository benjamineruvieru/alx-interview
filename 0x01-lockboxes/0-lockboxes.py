#!/usr/bin/python3
"""
Locked Boxes
"""

def canUnlockAll(boxes):
     '''
    Determines if all the boxes can be opened
    '''
    # Set to keep track of the boxes that can be opened
    opened = set([0])
    # List to store the keys of the current box
    keys = boxes[0]
    # Iterate until all boxes have been opened
    while len(opened) < len(boxes):
        # Iterate through the keys of the current box
        for key in keys:
            if 0 <= key < len(boxes) and key not in opened:
                # Add the key to the set of opened boxes
                opened.add(key)
                # Add the keys of the newly opened box to the list of keys
                keys += boxes[key]
        # If no new boxes were opened, all boxes cannot be opened
        if len(opened) == len(boxes):
            return True
    return False

