def sort_list(lst):
    if not lst:
        return []
    min_val = min(lst)
    max_val = max(lst)

    result = [max_val if x == min_val else min_val if x == max_val else x for x in lst]

    result.append(min_val)

    return result
print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))






