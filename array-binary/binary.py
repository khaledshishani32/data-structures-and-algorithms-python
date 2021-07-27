

def BinarySearch(my_list,target):
  for i in my_list :
    meddle_index =int((0+len(my_list)-1)/2)
    if target==my_list[meddle_index] :
        print(meddle_index)
        break
    if target>my_list[meddle_index]:
       meddle_index=int((meddle_index+len(my_list)-1)/2)
    elif target==my_list[meddle_index] :
        print(meddle_index)
        break
    if target< my_list[meddle_index]:
       meddle_index=int(meddle_index/2)
    if target==my_list[meddle_index] :
        print(meddle_index)
        break
    else :
        print(-1)
        break

BinarySearch([4, 8, 15, 16, 23, 42], 15)
BinarySearch([-131, -82, 0, 27, 42, 68, 179], 42)
BinarySearch([11, 22, 33, 44, 55, 66, 77], 90)
BinarySearch([1, 2, 3, 5, 6, 7], 4)





