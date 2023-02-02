#!/usr/bin/python3
"""
Locked Boxes
"""

def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened.
    '''
    if len(boxes[0]) == 0:
        return (False)
    keys = {0}
    size = len(boxes)
    visited = {0}
    keys = keys.union(boxes[0])
    while size > 0:
        for i in keys:
            if i in visited:
                continue
            keys = keys.union(boxes[i])
            visited.add(i)
        size -= 1
    return len(keys) == len(boxes)

