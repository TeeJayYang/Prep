cmds = []
with open('input') as file:
    cmds = file.readlines()


def execute(cmds):
    acc = 0
    seen = set()
    curr_line = 0

    while curr_line < len(cmds):
        if curr_line in seen:
            break
        seen.add(curr_line)
        instr, offset = cmds[curr_line].split()
        offset = int(offset)
        if instr == 'acc':
            acc += offset
            curr_line += 1
        elif instr == 'jmp':
            curr_line += offset
        elif instr == 'nop':
            curr_line += 1
    return acc, curr_line == len(cmds)


def makeFix(cmds):
    for i in range(len(cmds)):
        swap = False
        if 'nop' in cmds[i]:
            frm, to = 'nop', 'jmp'
            swap = True
        elif 'jmp' in cmds[i]:
            frm, to = 'jmp', 'nop'
            swap = True
        if swap:
            cmds[i] = cmds[i].replace(frm, to)
            acc, terminate = execute(cmds)
            if terminate:
                return acc
            cmds[i] = cmds[i].replace(to, frm)
    raise Exception('No valid fix')


# part 1
print(execute(cmds)[0])

# part 2
print(makeFix(cmds))
