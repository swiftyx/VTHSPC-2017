m, n = [int(a) for a in input().split(" ")]
lines = [input().split(" ") for _ in range(m)]
# lines[i][0] -> name
# skip lines[i][1]
lines = sorted(lines, key=lambda a: a[1])
MAX = 2 * n / m
schedule = [[] for _ in range(n)]
for line in lines:
    for i in range(2, len(line)):
        schedule[int(line[i]) - 1].append(line[0])
for a in schedule:
    print(a)