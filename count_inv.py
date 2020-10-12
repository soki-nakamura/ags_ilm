import re

def merge_and_count_inv(left_list, right_list):
    i = 0
    j = 0
    left_size = len(left_list)
    right_size =  len(right_list)
    n = left_size + right_size
    result_list = []
    split_inv = 0
    for k in range(0,n):
        if left_size <= i:
            result_list.extend(right_list[j:])
            break
        elif right_size <= j:
            result_list.extend(left_list[i:])
            break
        elif left_list[i] < right_list[j]:
            result_list.append(left_list[i])
            i += 1
        else:
            result_list.append(right_list[j])
            j += 1
            split_inv += len(left_list[i:])

    return result_list, split_inv

def sort_and_count_inv(input_list):
    size_of_input = len(input_list)
    if size_of_input == 0 or size_of_input == 1:
        return (input_list, 0)
    mid = int(size_of_input/2)
    left_list = input_list[:mid]
    right_list = input_list[mid:]

    C, left_inv = sort_and_count_inv(left_list)
    D, right_inv = sort_and_count_inv(right_list)
    B, split_inv = merge_and_count_inv(C,D)
    num_inv = left_inv + right_inv + split_inv

    return B, num_inv

with open('data/IntegerArray.txt') as f:
    text = f.readlines()

processed_text = [int(re.sub('\n','',t)) for t in text]
result = sort_and_count_inv(processed_text)
print(f'the number of inv is {result}')
