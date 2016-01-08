import numpy as np
import re


grid_x = 1000
grid_y = 1000

instructions = ['turn on', 'turn off', 'toggle']

grid = np.zeros((grid_x, grid_y))


def apply_operation(teststring):
    # x1, y1, x2, y2
    corners = [int(res) for res in re.findall(r'\d+', teststring)]
    instruction = None
    # turn on
    if instructions[0] in teststring:
        instruction = instr_turn_on
    # turn off
    elif instructions[1] in teststring:
        instruction = instr_turn_off
    # toggle
    else:
        instruction = instr_toggle
    for x in range(corners[0], corners[2] + 1):
        for y in range(corners[1], corners[3] + 1):
            instruction(grid, x, y)


def instr_turn_on(grid, pos_x, pos_y):
    grid[pos_x, pos_y] = 1


def instr_turn_off(grid, pos_x, pos_y):
    grid[pos_x, pos_y] = 0


def instr_toggle(grid, pos_x, pos_y):
    grid[pos_x, pos_y] = 0 if grid[pos_x, pos_y] == 1 else 1


with open("data.txt", 'r') as f:
    content = f.readlines()
    for line in content:
        apply_operation(line)
    print int(np.array(grid).sum())
