from itertools import combinations

f = open("input.txt", "r")
numbers = list(map(int, f.read().split()))

PREAMBLE_LEN = 25

# generate list of sums of all pairs in list
def pair_sums(nums):
    return list(map(lambda s: sum(s), combinations(nums, 2)))

"""given a list of numbers, find the first number where there isn't a pair sum equal to
it in the preceding <pre_len> numbers. return that number and it's idx"""
def find_missing_pair_in_preamble(nums, pre_len):
    # i want to try some sliding window approach but i'm unsure how to update and remove
    for i in range(pre_len, len(nums)):
        current_pairs = pair_sums(nums[i - pre_len : i])
        if nums[i] not in current_pairs:
            return (nums[i], i)

part_1_answer, part_1_idx = find_missing_pair_in_preamble(numbers, PREAMBLE_LEN)
print(f"PART 1: {part_1_answer}")

"""given a list of numbers and a target, find a continuous set of numbers summing
to target"""
def find_continuous_array_summing_to_target(nums, target):
    curr_sum = nums[0]
    left = 0
    right = 1
    l = len(nums)

    while right <= l:
        # we got bigger than our target, start shrinking the window from the left
        while curr_sum > target and left < right - 1:
            curr_sum -= nums[left]
            left += 1
        
        #possibly found a match
        if curr_sum == target:
            return nums[left: right]
        
        # we must be smaller than our target, grow the window from the right
        curr_sum += nums[right]
        right += 1
    # techincally don't need this since we know there's going to be an answer
    return None

part_2_set = find_continuous_array_summing_to_target(numbers[:part_1_idx], part_1_answer)

part_2_answer = min(part_2_set) + max(part_2_set)

print(f"PART 2: {part_2_answer}")