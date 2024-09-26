def selection_sort(array):
    for i in range(len(array)-1):
        current_min = i
        for j in  range(i+1 , len(array)):
            if array[current_min] > array[j]:
                temp = array[current_min]
                array[current_min] = array[j]
                array[j] = temp

array = [5,4,3,2,1]
print("Given array:", array)
selection_sort(array)
print("Sorted array:",array)