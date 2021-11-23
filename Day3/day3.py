f = open("input.txt", "r")

input_file = f.read().splitlines()

repeat_len = len(input_file[0])

def count_trees_hit(right, down):
    tree_hits = 0
    current_position = 0

    for i in range(0, len(input_file), down):
        row = input_file[i]
        if row[current_position] == "#":
            tree_hits += 1
        current_position = (current_position + right) % repeat_len
    return tree_hits

print("PART 1")
b = count_trees_hit(3, 1)
print(f"You hit {b} trees. Ouch.")

print("PART 2")
a = count_trees_hit(1, 1)
c = count_trees_hit(5, 1)
d = count_trees_hit(7, 1)
e = count_trees_hit(1, 2)
print(f"You hit {a} trees. Oof.")
print(f"You hit {b} trees. Ouch.")
print(f"You hit {c} trees. Yeouch.")
print(f"You hit {d} trees. Argh.")
print(f"You hit {e} trees. Ow.")
print(f"ANSWER {a * b * c * d * e}")

