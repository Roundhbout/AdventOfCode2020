import copy

f = open("input.txt", "r")

input_file = f.read().split('\n')

input_rules = list(map(lambda s : s.split(), input_file))[:-1]


def run_loop(rules):
    seen_idx = []
    i = 0
    acc = 0
    
    while i not in seen_idx and i < len(rules) - 1:
        seen_idx.append(i)
        curr_rule = rules[i]
        cmd, arg = curr_rule
        
        if cmd == 'jmp':
            i += int(arg)
            continue
        elif cmd == 'acc':
            acc += int(arg)
        i += 1
    return acc

# run through the loop as normal, if a jmp or nop is found, try actually running the loop modifying at that point
# return only if the loop naturally terminates
def try_all_possible_corruptions(rules):
    seen_idx = []
    i = 0
    while i not in seen_idx:
        seen_idx.append(i)
        curr_rule = rules[i]
        cmd, arg = curr_rule
        if cmd != 'acc':
            mod_attempt = run_loop_mod_at_index(rules, i)
            if mod_attempt is not None:
                return mod_attempt
            if cmd == 'jmp':
                i += int(arg)
                continue
        i += 1

    return "bababooie"

# this is the same as run_loop but will flip the command at idx
def run_loop_mod_at_index(rules, idx):
    seen_idx = []
    i = 0
    acc = 0

    while i not in seen_idx and i < len(rules):
        seen_idx.append(i)
        curr_rule = rules[i]
        cmd, arg = curr_rule

        # modify command at this index to see if it's the corrupted one
        if i == idx:
            if cmd == 'jmp':
                cmd = 'nop'
            else:
                cmd = 'jmp'
        
        if cmd == 'jmp':
            i += int(arg)
            continue
        elif cmd == 'acc':
            acc += int(arg)
        i += 1

    #determine what closed the loop
    if i > len(rules) - 1:
        return acc
    return None
def part_1():
    return run_loop(input_rules)

def part_2():
    fixed_rules = copy.deepcopy(input_rules)
    return try_all_possible_corruptions(fixed_rules)

print(f"PART 1: {part_1()}")
print(f"PART 2: {part_2()}")
