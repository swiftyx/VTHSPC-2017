s, n = [int(a) for a in input().split(" ")]
arr = [[i + 1, 0] for i in range(n)]
def won():
    if len(arr) > 2:
        return False
    if len(arr) == 1:
        return True
    return arr[0][0] == arr[1][0]
index = 0
while not won():
    index = (index + s - 1) % len(arr)
    v = arr[index][1]
    if v == 0:
        arr[index][1] = 1
        arr.insert(index, [arr[index][0], 1])
    elif v == 1:
        arr[index][1] = 2
        index += 1
    else:
        del arr[index]
print(arr[0][0])