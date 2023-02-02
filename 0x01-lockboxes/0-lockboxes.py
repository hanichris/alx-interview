#!/usr/bin/python3
"""Solve the lockboxes interview problem."""
from collections import deque


def canUnlockAll(boxes):
    """Determine whether all the boxes can be visited.

    Use bfs algorithm to explore all the boxes.
    Args:
        boxes (list of list): matrix where each row is
        a box with keys to other boxes.
    Return:
        boolean.
    """
    boxes_len = len(boxes)
    # Check for when array of boxes is empty.
    if boxes_len == 0:
        return False

    # Initially, mark all the boxes as not visited
    # and not processed.
    visited = [False] * boxes_len
    processed = [False] * boxes_len

    # Initialize an empty queue to keep track of the
    # keys to each box.
    queue = deque()

    # Mark the first box as visited and store all its keys in
    # the queue.
    visited[0] = True
    processed[0] = True
    queue.extend(boxes[0])
    while queue:
        key = queue.popleft()
        if key >= boxes_len or processed[key] is True:
            continue
        processed[key] = True
        box = boxes[key]
        for other_key in box:
            if other_key >= boxes_len:
                continue
            if visited[other_key] is False:
                queue.append(other_key)
                visited[other_key] = True

    return False not in processed
