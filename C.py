n, y = [int(a) for a in input().split(" ")]
got = set([int(input()) for _ in range(y)])
for i in range(n):
    if i not in got:
        print(i)
print("Mario got "+ str(len(got))+" of the dangerous obstacles.")