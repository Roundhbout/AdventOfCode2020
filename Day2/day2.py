
f = open("input.txt", "r")

input_file = f.readlines()

# takes in a pw policy and returns the important values
# '1-4 s' -> {'low' : 1, 'high' : 4, 'char' : 's'}
def parse_policy(p):
    r, char = p.split()
    low, high = map(int, r.split('-'))
    return {'low' : low, 'high' : high, 'char' : char}

# validates pw according to policy
def validate_password(policy, pw):
    return policy['low'] <= pw.count(policy['char']) <= policy['high']

def validate_password_2(policy, pw):
    return [pw[policy['low'] - 1], pw[policy['high'] - 1]].count(policy['char']) == 1

valids = 0
valids2 = 0
for line in input_file:
    p, pw = line.split(': ')
    policy = parse_policy(p)
    if validate_password(policy, pw):
        valids += 1 
    if validate_password_2(policy, pw):
        valids2 += 1

print(f"VALID PASSWORDS = {valids}")
print(f"PART TWO PASSWORD VALIDS = {valids2}")