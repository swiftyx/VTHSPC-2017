# TODO: Wrong Answer

from math import floor, ceil
l, w = [int(a) for a in input().split(" ")]

def ec(c):
    return ord(c) - 96
def ev(s):
    return sum([ec(c) for c in s])

def out(s):
    # print(len(s))
    # print(ev(s))
    print(s)

letters = sorted('qwertyuiopasdfghjklzxcvbnm')
val = [ec(c) for c in letters]
if l <= 0 or w <= 0 or l * 26 < w or w < l:
    print("impossible")
else:
    pending = w % l
    index = floor(w / l)
    arr = [index - 1 for _ in range(l)]
    for i in range(pending):
        arr[i] += 1
    s = "".join([letters[v] for v in arr])
    out(s)
