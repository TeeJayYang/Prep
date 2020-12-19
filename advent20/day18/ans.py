from operator import add, mul
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


# part 1
print(sum(parse1(expr, 0)[0] for expr in expressions))
