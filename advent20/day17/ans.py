space3d = set()
space4d = set()

with open('input') as file:
    for x, line in enumerate(file):
        for y, cube in enumerate(line.strip()):
            if cube == '#':
                space3d.add((x, y, 0))
                space4d.add((x, y, 0, 0))


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
        if n in space:
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
    for coord in space:
        # active cubes
        neighbours = get_neighbours(*coord)
        active_neighbours = count_active_neighbours(space, neighbours)
        if active_neighbours not in {2, 3}:
            flip.add(coord)

        # check if inactive neighbour should be flipped too
        for n in neighbours:
            if n in space:
                continue
            neighbours = get_neighbours(*n)
            active_neighbours = count_active_neighbours(space, neighbours)
            if active_neighbours == 3:
                flip.add(n)

    for coord in flip:
        if coord in space:
            space.remove(coord)
        else:
            space.add(coord)


def count_active(space, cycles):
    for i in range(cycles):
        execute(space)

    return len(space)


# part 1
print(count_active(space3d, 6))

# part 2
print(count_active(space4d, 6))
