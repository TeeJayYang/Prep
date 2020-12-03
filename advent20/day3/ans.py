field = []
width = 0
with open('input') as file:
    for line in file:
        # account for the \n
        width = len(line) - 1
        trees = set()
        for i in range(len(line)):
            if line[i] == '#':
                trees.add(i)
        field.append(trees)


def trees(field, width, right, down):
    pos = 0
    num_trees = 0
    for row in field[::down]:
        if pos in row:
            num_trees += 1
        pos = (pos + right) % width
    return num_trees


# part 1
print(trees(field, width, 3, 1))

# part 2
ans = 1
for i in (1, 3, 5, 7):
    ans *= trees(field, width, i, 1)
ans *= trees(field, width, 1, 2)
print(ans)
