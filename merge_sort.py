def merge_list(left_list, right_list):
    i = 0
    j = 0
    left_size = len(left_list)
    right_size =  len(right_list)
    n = left_size + right_size
    result_list = []
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

    return result_list


def merge_sort(input_list):

    size_of_input = len(input_list)
    if size_of_input == 1:
        return input_list

    mid = int(size_of_input/2)
    left_list = input_list[:mid]
    right_list = input_list[mid:]

    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge_list(left, right)
)
