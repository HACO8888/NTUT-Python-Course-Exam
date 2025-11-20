def longest_increasing(nums):
    if not nums:
        return [], 0

    max_length = 1
    current_length = 1
    max_start_index = 0
    current_start_index = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
        else:
            current_length = 1
            current_start_index = i

    longest_sequence = nums[max_start_index:max_start_index + max_length]
    return longest_sequence, max_length

user_input = input("Enter a list of numbers: ")

if user_input.strip().startswith('[') and user_input.strip().endswith(']'):
    numbers_str = user_input.strip()[1:-1]
    input_list = [int(x.strip()) for x in numbers_str.split(',')]
else:
    input_list = list(map(int, user_input.split()))

sequence, length = longest_increasing(input_list)
print(f"The longest increasing sequence is {sequence}, so the length is {length}.")

