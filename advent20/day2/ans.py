lines = []
with open('input') as file:
    for line in file:
        lines.append(line.split())


def passcheck1(lines):
    count = 0
    for line in lines:
        bot, top = map(int, line[0].split('-'))
        letter = line[1][0]
        if bot <= line[2].count(letter) <= top:
            count += 1
    return count


def passcheck2(lines):
    count = 0
    for line in lines:
        bot, top = map(int, line[0].split('-'))
        letter = line[1][0]
        if ((line[2][bot - 1] == letter) + (line[2][top - 1] == letter)) == 1:
            count += 1
    return count


print(len(lines))
print(passcheck1(lines))
print(passcheck2(lines))
