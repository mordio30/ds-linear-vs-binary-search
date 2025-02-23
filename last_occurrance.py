# Linear Search
def linear_search_last_occurrence(arr, target):
    # Your code here
    steps = 0
    last_index = -1
    for i, element in enumerate(arr):
        steps += 1
        if target == element:
            last_index = i
    return last_index, steps

# Binary Search
def binary_search_last_occurrence(arr, target):
    # Your code here
    steps = 0
    last_index = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            last_index = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_index, steps

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")