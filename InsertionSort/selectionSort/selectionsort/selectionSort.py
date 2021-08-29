def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index=i
        for j in range(i+1 , len(my_list)):
            if my_list[min_index]>my_list[j]:
              min_index= j
        my_list[i],my_list[min_index]= my_list[min_index] ,my_list[i]
    print(my_list)      


cus_list=[8,4,23,42,16,15]

selection_sort(cus_list)
