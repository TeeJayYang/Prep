from operator import add, mul
from functools import reduce

with open('input') as file:
    expressions = [line.strip() for line in file]


def parse1(expr, idx):
    op_map = {
        '+': add,
        '*': mul,
    }

    ans = None
    prev_op = None

    while idx < len(expr):
        c = expr[idx]
        if c == ')':
            break
        elif c == ' ':
            pass
        elif c.isnumeric():
            c = int(c)
            if ans is None:
                ans = c
            else:
                ans = prev_op(ans, c)
        elif c in op_map:
            prev_op = op_map[c]
        elif c == '(':
            sub_ans, idx = parse1(expr, idx + 1)
            if ans is None:
                ans = sub_ans
            else:
                ans = prev_op(ans, sub_ans)
        else:
            raise Exception(f'Cannot parse {c}')
        idx += 1
    return ans, idx


def parse2(expr, idx):
    ans = []

    last_sum = None

    while idx < len(expr):
        c = expr[idx]
        if c == ')':
            break
        elif c == ' ':
            pass
        elif c == '+':
            pass
        elif c.isnumeric():
            c = int(c)
            if last_sum is None:
                last_sum = c
            else:
                last_sum += c
        elif c == '*':
            ans.append(last_sum)
            last_sum = None
        elif c == '(':
            sub_ans, idx = parse2(expr, idx + 1)
            if last_sum is None:
                last_sum = sub_ans
            else:
                last_sum += sub_ans
        else:
            raise Exception(f'Cannot parse {c}')
        idx += 1
    ans.append(last_sum)
    return reduce(mul, ans), idx


# part 1
# print(sum(parse1(expr, 0)[0] for expr in expressions))

# part 2
print(sum(parse2(expr, 0)[0] for expr in expressions))
