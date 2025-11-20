def is_arithmetic_sequence(lst):
    if len(lst) < 2:
        return True
    
    common_difference = lst[1] - lst[0]
    
    for i in range(1, len(lst) - 1):
        if lst[i + 1] - lst[i] != common_difference:
            return False
            
    return True
  
test_list1 = [2, 4, 6, 8, 10]
test_list2 = [1, 2, 4, 8]
print(f"{test_list1} is arithmetic sequence: {is_arithmetic_sequence(test_list1)}")
print(f"{test_list2} is arithmetic sequence: {is_arithmetic_sequence(test_list2)}")