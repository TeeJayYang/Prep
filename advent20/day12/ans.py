from collections import namedtuple

Instruction = namedtuple('Instruction', 'action, value')
Index = namedtuple('index', 'x, y')
Directions = namedtuple('directions', 'N, NE, E, SE, S, SW, W, NW')
directions = Directions(N=Index(0, 1),
                        NE=Index(1, 1),
                        E=Index(1, 0),
                        SE=Index(1, -1),
                        S=Index(0, -1),
                        SW=Index(-1, -1),
                        W=Index(-1, 0),
                        NW=Index(-1, 1))

instructions = []
with open('input') as file:
    for line in file:
        instructions.append(Instruction(line[0], int(line[1:].strip())))


def addIndex(one, two, times=1):
    return Index(one.x + two.x * times, one.y + two.y * times)


def execute(instructions):
    headings = ('N', 'E', 'S', 'W')
    heading_idx = 1
    pos = Index(0, 0)
    for instr in instructions:
        if instr.action in headings:
            pos = addIndex(pos, getattr(directions, instr.action), instr.value)
        elif instr.action == 'F':
            pos = addIndex(pos, getattr(directions,
                                        headings[int(heading_idx)]),
                           instr.value)
        elif instr.action == 'R':
            heading_idx += instr.value / 90
            heading_idx %= 4
        elif instr.action == 'L':
            heading_idx -= instr.value / 90
            heading_idx %= 4
    return pos


def execute2(instructions):
    headings = ('N', 'E', 'S', 'W')
    waypoint = Index(10, 1)  # 10 east 1 north
    pos = Index(0, 0)
    for instr in instructions:
        if instr.action in headings:
            waypoint = addIndex(waypoint, getattr(directions, instr.action),
                                instr.value)
        elif instr.action == 'F':
            pos = addIndex(pos, waypoint, instr.value)
        elif instr.action == 'R':
            turns = instr.value / 90
            for i in range(int(turns)):
                waypoint = Index(waypoint.y, -waypoint.x)
        elif instr.action == 'L':
            turns = instr.value / 90
            for i in range(int(turns)):
                waypoint = Index(-waypoint.y, waypoint.x)
    return pos


# part1
final_pos = execute(instructions)
print(abs(final_pos.x) + abs(final_pos.y))

# part 2
final_pos = execute2(instructions)
print(abs(final_pos.x) + abs(final_pos.y))
