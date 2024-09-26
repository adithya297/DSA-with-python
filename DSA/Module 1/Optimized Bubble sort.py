def bubble_sort(array):
    for i in range(len(array)-1):
        sorted=False
        for j in  range(len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                sorted=True
        if not sorted:
            if i == 0:
                print("Array is already sorted")
                break
n=int(input("Enter the number of elements in array: "))
array = []
for k in range(n):
    element = int(input(f"Enter the element for index {k}: "))
    array.append(element)

print("Given Array:",array)

bubble_sort(array)
print("Sorted array:",array)