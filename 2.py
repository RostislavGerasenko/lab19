from collections import Counter

n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the first array: ")) for i in range(n)]
count = Counter(arr)
for item, amount in count.items():
    if amount == 2:
        arr.remove(item)
        arr.remove(item)
print(f"Length of the array: {len(arr)}. Array: {arr}")
