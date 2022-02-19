"""
Exercise 2
"""

# PART 1: Gather Information
# - Expected outputs (sequentially) are False and True. Actual results are False and False.
# - There is no traceback/error, which means the problem might be a logic error.
# - The problematic lines are in the flow of the conditional that checks if numbers are consecutive.

# PART 2: State Assumptions
# - Within the conditional statement, we assume that the loop will repeat itself for each index in the loop range.
#   If we test this out, we see that actually what's happening is that the function terminates
#   after just one conditional check. This is because there is a return statement in all branches of the if statement.
#   This must be the source of the bug.

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else:
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True