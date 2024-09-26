def selection_sort(array):
    for i in range(len(array)-1):
        current_min = i
        for j in range(i+1,len(array)):
            if array[j] < array[current_min]:
                current_min = j
        temp = array[i]
        array[i] = array[current_min]
        array[current_min] = temp

n=int(input("Enter the number of elements in array: "))
array = []

for i in range(n):
    element = int(input(f"Enter the element for index {i}:"))
    array.append(element)

print("Array:",array)
selection_sort(array)
print(array)
