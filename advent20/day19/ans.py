from itertools import product as cartesian_product
import inspect
import re

with open('input') as file:
    messages = []
    rules = {}
    rule_pattern = re.compile(r'(\d+): (.+)')
    while True:
        line = file.readline()
        rule_line = rule_pattern.match(line)
        if rule_line:
            rules[rule_line.group(1)] = rule_line.group(2)
        else:
            break

    messages = [line.strip() for line in file]

longest_string = max(map(len, messages))


def get_valid_strings(rules, rule_name):
    if isinstance(rules[rule_name], set):
        return rules[rule_name]

    rule = rules[rule_name]
    if '"' in rule:
        return {rule.strip(' "')}
    else:
        matches = [match.strip() for match in rule.split('|')]
        valid_strings = set()
        for match in matches:
            if rule_name in match.split() and len(inspect.stack(0)) > 3:
                continue
            sub_valid_strings = []
            for sub_rule in match.split():
                sub_valid_strings.append(get_valid_strings(rules, sub_rule))
            for permutation in cartesian_product(*sub_valid_strings):
                valid_strings.add(''.join(permutation))
        rules[rule_name] = valid_strings
    return valid_strings


# part 1
valid_strings = get_valid_strings(rules, '0')
valid_messages = [message for message in messages if message in valid_strings]
print(len(valid_messages))

# part 2 (maybe switch to using regex)
rules['8'] = '42 | 42 8'
rules['11'] = '42 31| 42 11 31'
# valid_strings = get_valid_strings(rules.copy(), '0')
# valid_messages = [message for message in messages if message in valid_strings]
# print(len(valid_messages))
