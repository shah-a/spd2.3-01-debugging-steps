"""
Exercise 4
"""

# PART 1: Gather Information
# - The expected output is the index where the search target exists in the array. In this, index 4. The actual output is an error for maximum recursion depth exceeded.
#   - The error means that there's a flaw in our routing logic that causes infinite recursion.
# - The lines in our if-structure where we recursively call `binary_search()` are the lines that are causing the error.
# - The cause of the error must be that the parameters being passed are not satisfying the condition for the recursion to terminate.

# PART 2: State Assumptions
# - We assume that each time we recurse, the mid-point of our search is half-way between the previous mid-point.
# - In the lines where we called `binary_search()`, we assume that the new midpoint is different than the previous midpoint as we traverse through the indices.
#   - This is the source of the bug. Eventually we hit a point where the midpoint is the same as the previous midpoint, causing infinite recursion.
#   - This can be fixed by setting the `high` value to `mid - 1` if arr[mid] > element and by setting `low` to `mid + 1` if arr[mid] < element.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        return binary_search(arr, element, mid, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)