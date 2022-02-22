"""
Exercise 3
"""

# PART 1: Gather Information
# - The input array is [5, 2, 3, 1, 6], so the expected output is [1, 2, 3, 5, 6]. The actual result is an error.
# - The error message specifies that the problem is an IndexError (index out of range) on the line where `key` is compared to `arr[j]`
# - Within the while loop, `j` is decremented. This causes arr[j] in the `while` statement to eventually be arr[-6].
# - There are only 5 elements in the array, so arr[-6] must be causing the error

# PART 2: State Assumptions
# - As `i` traverses each array element, we assume that `j` in the while loop goes from `i-1` to 0.
#   - If we test this, we see that `j` eventually passes 0 and enters the range of negative integers. This is the source of the bug.
#     We can confirm by adding `j >= 0` as a condition to the while loop to test if it solves the bug.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

