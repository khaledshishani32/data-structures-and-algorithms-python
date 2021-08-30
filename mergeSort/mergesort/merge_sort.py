

def merge(input_list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = input_list[l+i]
    
    for j in range(0, n2):
        R[j] = input_list[m+1+j]
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            input_list[k] = L[i]
            i += 1
        else:
            input_list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        input_list[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        input_list[k] = R[j]
        j += 1
        k += 1

def merge_sort(input_list, l, r):
    if l < r:
        m = (l+(r-1))//2
        merge_sort(input_list, l, m)
        merge_sort(input_list, m+1, r)
        merge(input_list, l, m, r)
    return input_list

	

my_list = [30,27,43,3,9,62,10]

print(merge_sort(my_list , 0 ,6))


