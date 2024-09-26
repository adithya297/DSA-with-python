def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j-1] > array[j] and j > 0:
            array[j-1] , array[j] = array[j], array[j-1]
            j -= 1

array = [5,4,3,2,1]
print("Given array", array)
insertion_sort(array)
print("Sorted array:", array)