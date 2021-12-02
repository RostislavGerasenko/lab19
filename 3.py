n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the first array: ")) for i in range(n)]
minimum = min(arr)
maximum = max(arr)
arr.insert(arr.index(minimum), 0)
arr.insert(arr.index(maximum) + 1, 0)
print(f"Array: {arr}")
