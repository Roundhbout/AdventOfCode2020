from functools import lru_cache

f = open("input.txt", "r")

adapters = list(map(int, f.read().split()))

phone_rating = max(adapters) + 3

# we count the difference from the last adapter to the phone, so include that in the list
adapters.append(phone_rating)
# we ALSO count the different from the port to the first adapter, so include that too
adapters.append(0)

"""sort the adapters so we know that we need to connect adapters[i] 
to adapters[i + 1] (and that it will connect without causing a fire)"""
adapters.sort()

"""get the differences in joltage by taking an adapter rating from the list and subtracting
    the previous adapter rating"""
joltage_diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]

# count the number of 1 differences and 3 differences
one_jolt_diffs = joltage_diffs.count(1)
three_jolt_diffs = joltage_diffs.count(3) 

print(f"PART 1: {one_jolt_diffs * three_jolt_diffs}")

#--------------------------------------------------
# had to look up a solution but this does make sense
@lru_cache(maxsize=256)
def recursive_paths_to_end(i):
    # if we're at the last adapter, there's only one path left (that we took)
    if i == len(adapters) - 1:
        return 1
    """
    return the sum of this function called across every adapter within 3 spaces
    (or less if we're at the end of the list) if the joltage difference is at most
    three.
    """
    return sum(
        [
            recursive_paths_to_end(j)
            for j in range(i + 1, min(i + 4, len(adapters)))
            if adapters[j] - adapters[i] <= 3
        ]
    )

"""
seems like lru_cache stores values seen in previous iterations
Least_Recently_Used cache evicts the key-value used the least when it needs more space.

the cache is a decorator that basically stores results of the function call in a dict.
the args must be hashable.
"""

print(f"PART 2: {recursive_paths_to_end(0)}")
