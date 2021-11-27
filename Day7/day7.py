#https://www.globalnerdy.com/2020/12/14/my-solution-to-advent-of-code-2020s-day-7-challenge-in-python/
import pprint

f = open("input.txt", "r")

input_file = f.readlines()

rules = dict(map(lambda s : s.split(' bags contain '), input_file))

#this is an abomination but it's what i know how to do
def parse_contains(contains):
    #remove trailing newline and period
    contains = contains.rstrip('.\n')
    # separate each bag and count into own element
    bags = contains.split(', ')
    # separate the bag color and the count of said bag per bag_type
    num_bags = list(map(lambda b : b.split(maxsplit=1), bags))
    # format bag color and count (trim 'bag'/'bags', convert count to int), ignore bags that don't contain other bags
    formatted_num_bags = [[int(num), bag_type.rsplit(' ', 1)[0]] for num, bag_type in num_bags if num != 'no']
    # key list for zipping
    keys = ['num', 'bag_type']
    # zip the keys to each count/bag color instance
    keys_num_bags = [list(zip(keys, num_bag)) for num_bag in formatted_num_bags]
    # create a dict given the now zipped key value tuples

    bag_contains = [dict(zb) for zb in keys_num_bags]
    """
    This function takes:
        2 striped silver bags, 4 mirrored maroon bags, 5 shiny gold bags, 1 dotted gold bag.
    and returns
        [{'num': 2, 'bag_type': 'striped silver'}, {'num': 4, 'bag_type': 'mirrored maroon'},
         {'num': 5, 'bag_type': 'shiny gold'}, {'num': 1, 'bag_type': 'dotted gol'}]
    """
    return bag_contains

# need to do a recursive approach to figure things out
"""
args: all_bags (parsed input in it's entirety), current_bag(str of current bag type)
return number of shiny gold bags contained in current_bag
"""
def target_bag_count(all_bags, current_bag, target_bag):
    count = 0
    bag_contents = all_bags[current_bag]
    if len(bag_contents) == 0:
        return count
    else:
        for sub_bag in bag_contents:
            if sub_bag['bag_type'] == target_bag:
                count += 1
            count += target_bag_count(all_bags, sub_bag['bag_type'], target_bag)
    return count

# returns number of bag colors that contain at least one shiny gold bag
def bags_containing_shiny_gold(all_bags):
    count = 0
    for bag_name in all_bags.keys():
        if target_bag_count(all_bags, bag_name, 'shiny gold'):
            count += 1
    return count

"""
Return the number of bags contained within target bag
"""
def bags_inside_target(all_bags, target):
    #init count, get current bag + it's content info from all_bags
    count = 0
    curr_bag = all_bags[target]
    #if the bag is empty, return count (should be 0)
    if len(curr_bag) == 0:
        return count
    # current bag contains at least one other type of bag of any given count
    else:
        # for ever sub bag in target
        for bag in curr_bag:
            # get the amount of sub bags and add it to the count
            curr_bag_count = bag['num']
            count += curr_bag_count
            # get the amount of bags within a given sub bag, add that multiplied by the number of sub bags to count
            bags_inside_curr_bag = bags_inside_target(all_bags, bag['bag_type'])
            count += bags_inside_curr_bag * curr_bag_count

    return count


parsed_rules = {bag : parse_contains(contains) for bag, contains in rules.items()}

def part_1():
    return bags_containing_shiny_gold(parsed_rules)

def part_2():
    return bags_inside_target(parsed_rules, 'shiny gold')

print(f"PART 1: {part_1()}")
print(f"PART 2: {part_2()}")