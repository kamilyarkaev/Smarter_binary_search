mylist = [1, 2, 8, 8, 8, 8, 9, 10]
target = 8
new_start, new_end = None, None
counter = 0
first_index = 0
last_index = 0

def binary_search(mylist, target):
    start, end = 0, len(mylist) - 1
    dif_num_indexes = []
    while start <= end:
        mid = (start + end) //2
        if mylist[mid] == target:
            global first_index
            first_index = mid   
            end = mid-1




        if mylist[mid] < target:
            start = mid + 1
        
        if mylist[mid] > target:
            end = mid - 1


    start, end = 0, len(mylist) - 1
    while start <= end:
        mid = (start + end) //2
        if mylist[mid] == target:
            global last_index
            last_index = mid   
            start = mid+1




        if mylist[mid] < target:
            start = mid + 1
        
        if mylist[mid] > target:
            end = mid - 1
    if first_index == last_index:
        print(f"There is only one target in the list and it's index is {first_index}")
    else:
        print(f"The target, {target}, was found on the range of indexes from {first_index} to {last_index}")
        for x in range(first_index, last_index+1):
            dif_num_indexes.append(x)
        print(f"Here's the list of all the indexes where the target, {target}, was found: {dif_num_indexes}")



list_with_100_items = [146, 161, 193, 217, 266, 276, 460, 487, 585, 756, 842, 889, 954, 985, 1061, 1114, 1169, 1256, 1509, 1533, 1680, 1829, 1917, 1995, 2013, 2085, 2134, 2182, 2249, 2261, 2306, 2499, 2543, 2723, 2731, 3196,3196,3196,3196,3196,3196,3196,3196,3196,3196, 3253, 3271, 3351, 3514, 3557, 3629, 3755, 3884, 3935, 4163, 4236, 4296, 4298, 4420, 4661, 4764, 4891, 5020, 5149, 5278, 5407, 5536, 5665, 5794, 5923, 6052, 6181, 6310, 6439, 6568, 6697, 6826, 6955, 7084, 7213, 7342, 7471, 7600, 7729, 7858, 7987, 8116, 8245, 8374, 8503, 8632, 8761, 8890, 9019, 9148, 9277, 9406, 9535, 9664, 9793, 9922]



new_target = 3196
binary_search(list_with_100_items, new_target)








binary_search(mylist, target)
