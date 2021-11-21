
"""
Using a two pointer approach
"""
f = open("input.txt", "r")

input_file = f.readlines()

numbers = sorted(list(map(lambda s: int(s[:-1]), input_file)))

target = 2020


def find_pair_summing_to_target(nums, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        attempt = nums[left] + nums[right]
        if attempt == target:
            return (nums[left], nums[right])
        elif attempt < target:
            left += 1
        else:
            right -= 1
    return None

num1, num2 = find_pair_summing_to_target(numbers, target)
answer = num1 * num2
print(f"ANSWER: {answer}")






