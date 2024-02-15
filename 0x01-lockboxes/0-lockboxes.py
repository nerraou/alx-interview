#!/usr/bin/python3
"""determines if all the boxes can be opened"""

def visit_box(box, boxes, visited):
    """visit a box recursively"""
    for key in box:
        if key < len(boxes) and key not in visited:
            visited.add(key)
            visit_box(boxes[key], boxes, visited)


def canUnlockAll(boxes):
    """can unlock all boxes"""
    visited_boxes = set([0])

    visit_box(boxes[0], boxes, visited_boxes)

    if len(visited_boxes) == len(boxes):
        return True

    return False
