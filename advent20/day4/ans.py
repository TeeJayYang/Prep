import re

mand_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passports = []
with open('input') as file:
    passport = {}
    for line in file:
        if line == '\n':
            passports.append(passport)
            passport = {}
        fields = dict(map(lambda x: tuple(x.split(':')), line.split()))
        passport.update(fields)
    passports.append(passport)


def validate_passport(passport):
    for k, v in passport.items():
        if k == 'byr' and not (1920 <= int(v) <= 2002):
            return False
        elif k == 'iyr' and not (2010 <= int(v) <= 2020):
            return False
        elif k == 'eyr' and not (2020 <= int(v) <= 2030):
            return False
        elif k == 'hgt':
            match = re.search(r'([0-9]+)(cm|in)', v)
            if not match:
                return False

            height = int(match.group(1))
            cm_in = match.group(2)
            if (cm_in == 'cm' and not (150 <= height <= 193)
                    or cm_in == 'in' and not (59 <= height <= 76)):
                return False
        elif k == 'hcl':
            if not re.match(r'#([0-9a-f]){6}', v):
                return False
        elif k == 'ecl':
            if not (v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
                return False
        elif k == 'pid':
            if not re.match(r'[0-9]{9}', v):
                return False
    return True


def valid_passports(mand_fields, passports, part1=True):
    count = 0
    for passport in passports:
        if passport.keys() & mand_fields == mand_fields:
            if part1 or validate_passport(passport):
                count += 1
    return count


print(valid_passports(mand_fields, passports))
print(valid_passports(mand_fields, passports, False))
