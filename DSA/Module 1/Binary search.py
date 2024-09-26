def binary_search(array, key):
    low = 0
    high = len(array)-1
    found = False
    while low <= high:
        mid = (low+high)//2
        if key == array[mid]:
            print("Key found at index:",mid)
            found=True
            break
        elif key > array[mid]:
            low = mid+1
        else:
            high = mid-1
    if not found:
        print("Key not found")

n=int(input("Enter the number of elements in array: "))
array = []
for i in range(n):
    element = int(input("Enter the element:"))
    array.append(element)
print("Array:",array)

array.sort()
key = int(input("Enter the key: "))
binary_search(array,key)