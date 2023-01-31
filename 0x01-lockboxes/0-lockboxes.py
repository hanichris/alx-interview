#!/usr/bin/python3
"""Solve the lockboxes interview problem."""
from collections import deque


def canUnlockAll(boxes):
    """Determine whether all the boxes can be opened.

    Use bfs algorithm to explore all the boxes.
    Args:
        boxes (list of list): matrix where each row is
        a box with keys to other boxes.
    Return:
        boolean.
    """
    # Initially, mark all the boxes as not opened.
    opened = [False] * len(boxes)

    # Initialize an empty queue to track current box that is
    # open.
    queue = deque()

    # Mark the first box as opened and store all its keys in
    # a queue.
    opened[0] = True
    queue.extend(boxes[0])
    while queue:
        key = queue.popleft()
        opened[key] = True
        box = boxes[key]
        for new_key in box:
            if opened[new_key] is False:
                queue.append(new_key)
                opened[new_key] = True

    return False if False in opened else True
