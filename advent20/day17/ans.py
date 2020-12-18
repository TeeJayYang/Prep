space3d = {}
space4d = {}

with open('input') as file:
    x = 0
    for line in file:
        for y, cube in enumerate(line.strip()):
            if cube == '#':
                space3d[x, y, 0] = True
                space4d[x, y, 0, 0] = True
        x += 1


def get_neighbours(x, y, z, w=None):
    neighbours = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                nx = x + i
                ny = y + j
                nz = z + k
                if w is not None:
                    for m in (-1, 0, 1):
                        if i == j == k == m == 0:
                            continue
                        nw = w + m
                        neighbours.append((nx, ny, nz, nw))
                else:
                    if i == j == k == 0:
                        continue
                    neighbours.append((nx, ny, nz))
    return neighbours


def count_active_neighbours(space, neighbours):
    count = 0
    for n in neighbours:
        if space.get(n, False):
            count += 1
    return count


def should_flip(active, active_neighbours):
    if active and active_neighbours not in {2, 3}:
        return True
    elif not active and active_neighbours == 3:
        return True
    return False


def execute(space):
    flip = set()
    for coord, cube in space.items():
        neighbours = get_neighbours(*coord)
        active_neighbours = count_active_neighbours(space, neighbours)
        if cube and should_flip(cube, active_neighbours):
            flip.add(coord)

        # check if neighbour should be flipped too
        for n in neighbours:
            if space.get(n, False):
                continue
            neighbours = get_neighbours(*n)
            active_neighbours = count_active_neighbours(space, neighbours)
            if should_flip(space.get(n, False), active_neighbours):
                flip.add(n)

    for coord in flip:
        space[coord] = not space.get(coord, False)


def count_active(space, cycles):
    for i in range(cycles):
        execute(space)

    return list(space.values()).count(True)


# part 1
print(count_active(space3d, 6))

# part 2
print(count_active(space4d, 6))
