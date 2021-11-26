f = open("input.txt", "r")

input_file = f.read()

groups = input_file.split("\n\n")

def count_unique_questions(group):
    unique_yesses = set()
    people = group.split("\n")
    
    for p in people:
        for question in p:
            unique_yesses.add(question)
    
    return len(unique_yesses)

# For some reason group.split("\n") returns 3 less than the correct answer
def count_all_yes_questions(group):
    people = group.split()
    
    yesses = set.intersection(*map(set, people))
    return len(yesses)

def part_1():
    total_yesses = 0
    for g in groups:
        total_yesses += count_unique_questions(g)
    return total_yesses

def part_2():
    total_yesses = 0
    for g in groups:
        total_yesses += count_all_yes_questions(g)
    return total_yesses

print(f"PART 1: {part_1()}")
print(f"PART 2: {part_2()}")