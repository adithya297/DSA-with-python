def bubble_sort(array):
    for i in range(len(array)-1): #For number of passes
        swap = False #Flag variable if array is already sorted
        for j in range(len(array)-i-1): #For number of comparisions
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j] #Swapping elements
                swap = True
        if not swap:
            if i == 0:
                print("Array is already sorted")
            break

array = [5,4,3,2,1]
print("Given Array: ", array)
bubble_sort(array)
print("Sorted Array:", array)
    
