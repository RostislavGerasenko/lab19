n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(n)]
for index, element in enumerate(arr):
    if element > 0:
        arr.insert(index, 0)
print(f"Array: {arr}")
