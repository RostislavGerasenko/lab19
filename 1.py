n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(n)]
for i in range(len(arr)-1, 0, -1):
    if arr[i] == arr[i-1]:
        del arr[i]
print(f"Array: {arr}")
