def partition(my_list, low, high):
    i = low - 1
    pivot = my_list[high]
    for j in range(low,high):
        if my_list[j] <= pivot:
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
    my_list[i+1], my_list[high] = my_list[high], my_list[i+1]
    return (i+1)

def quick_sort(my_list, low, high):
    if low < high:
        partitions = partition(my_list, low, high)
        quick_sort(my_list, low, partitions-1)
        quick_sort(my_list, partitions+1, high)
    return my_list    


my_list=[8,4,23,42,16,15]

print(quick_sort(my_list , 0 , 5))

