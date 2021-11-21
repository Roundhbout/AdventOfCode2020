f = open("input.txt", "r")

input_file = f.readlines()

numbers = sorted(list(map(lambda s: int(s[:-1]), input_file)))

target = 2020

def find_triplet_summing_to_target(nums, target):
    for i in range(len(nums) - 1):
        s = set()
        curr_sum = target - nums[i]
        for j in range(i + 1, len(nums)):
            attempt = curr_sum - nums[j]
            if attempt in s:
                return (nums[i], nums[j], attempt)
            s.add(nums[j])
    return None

num1, num2, num3 = find_triplet_summing_to_target(numbers, target)

answer = num1 * num2 * num3

print(f"ANSWER: {answer}")