# Linear Search
def linear_search_sorted_words(word_list, target_word):
    # Your code here
    steps = 0
    for i, element in enumerate(word_list):
        steps += 1
        if target_word == element:
            return i, steps
    return -1, steps

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    # Your code here
    steps = 0
    left = 0
    right = len(word_list) - 1
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if word_list[mid] == target_word:
            return mid, steps
        elif word_list[mid] < target_word:
            left = mid + 1
        else:
            right = mid - 1
    return -1, steps

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")