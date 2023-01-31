# Lock Boxes.

Given ```n``` number of boxes, each numbered sequentially from ```0``` to ```n-1```, where each
box contains keys to other boxes, determine whether all the boxes can be opened.

Requirements:
- function prototype: ```def canUnlockAll(boxes)```
- ```boxes``` is a list of lists.
- Key with the same number as a box opens that box.
- Assume all keys are positive integers.
    - There can be keys that don't open any box.
- The first box, `box[0]`, is already open.
- Return ```true``` if all the boxes can be open. Otherwise, return ```false```.
