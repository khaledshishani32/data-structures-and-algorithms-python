





def insertShiftArray(arr , val):
    if(len(arr) % 2 ==0):
     index = int(len(arr) / 2)
     return arr[:index] + [val] + arr[index:]
    else:
     index = int(len(arr) / 2) +1
     return arr[:index] + [val] + arr[index:]
     

print(insertShiftArray([2,4,6,-8], 5))
print("------------------")
print(insertShiftArray([42,8,15,23,42], 16))