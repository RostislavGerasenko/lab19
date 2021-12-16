n = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(n)]
flag = False
for index, element in enumerate(arr):
    if flag:
        flag = False
        continue
    if element > 0:
        flag = True
        arr.insert(index, 0)
        index += 1
print(f"Array: {arr}")
