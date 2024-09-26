def linear_search(array,key):
    found=False
    for i in range(len(array)):
        if key == array[i]:
            print("Key found at index:",i)
            found=True
            break
    if not found:
        print("Key not found")
    

n=int(input("Enter the number of elements in array: "))
array = []
for i in range(n):
    element = int(input("Enter the element:"))
    array.append(element)
print("Array:",array)

key=int(input("Enter the key:"))
linear_search(array,key)