import re

f = open("input.txt", "r")

input_file = f.read()

passports = [dict(map(lambda s : s.split(':'), p.split())) for p in input_file.split("\n\n")]

def validate_passport_1(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all([field in passport.keys() for field in required_fields])

initial_valid_passports = [p for p in passports if validate_passport_1(p)]

print(f"Pt. 1 Valid passports: {len(initial_valid_passports)}")
#----------------------------------------------------------------------------------------------

def validate_byr(val):
    return val.isnumeric() and 1920 <= int(val) <= 2002 and len(val) == 4

def validate_iyr(val):
    return val.isnumeric() and 2010 <= int(val) <= 2020 and len(val) == 4

def validate_eyr(val):
    return val.isnumeric() and 2020 <= int(val) <= 2030 and len(val) == 4

def validate_hgt(val):
    if len(val) < 4:
        return False
    units = val[-2:]
    
    num = int(val[:-2])
    
    if units == 'in':
        return 59 <= num <= 76
    elif units == 'cm':
        return 150 <= num <= 193
    else:
        return False

def validate_hcl(val):
    pattern = re.compile(r"^#(?:[0-9a-f]{6})$")

    return re.fullmatch(pattern, val)
    
def validate_ecl(val):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return val in valid_colors

def validate_pid(val):
    return val.isnumeric() and len(val) == 9


"""given the already thought to be valid passports (to save on time)
    return those that are actually valid according to each field's rules"""
def validate_passport_2(passport):
    functions = {
        'byr' : validate_byr,
        'iyr' : validate_iyr,
        'eyr' : validate_eyr,
        'hgt' : validate_hgt,
        'hcl' : validate_hcl,
        'ecl' : validate_ecl,
        'pid' : validate_pid
    }
    verification = [functions.get(field, lambda x: True)(value) for field, value in passport.items()]
   
    
    return all(verification)



actually_valid_passports = [p for p in initial_valid_passports if validate_passport_2(p)]

print(f"Pt. 2 Valid Passports: {len(actually_valid_passports)}")