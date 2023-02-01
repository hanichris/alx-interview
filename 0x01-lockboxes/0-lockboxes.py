#!/usr/bin/python3
"""Solve the lockboxes interview problem."""


def canUnlockAll(boxes):
    """Determine whether all the boxes can be visited.

    Use bfs algorithm to explore all the boxes.
    Args:
        boxes (list of list): matrix where each row is
        a box with keys to other boxes.
    Return:
        boolean.
    """
    # Check for when array of boxes is empty.
    if len(boxes) == 0:
        return False

    # Initially, mark all the boxes as not visited
    # and not processed.
    visited = [False] * len(boxes)
    processed = [False] * len(boxes)

    # Initialize an empty queue to keep track of the
    # keys to each box.
    queue = []

    # Mark the first box as visited and store all its keys in
    # the queue.
    visited[0] = True
    processed[0] = True
    queue.extend(boxes[0])
    while queue:
        key = queue.pop(0)
        processed[key] = True
        box = boxes[key]
        for new_key in box:
            if visited[new_key] is False:
                queue.append(new_key)
                visited[new_key] = True

    return False not in processed
