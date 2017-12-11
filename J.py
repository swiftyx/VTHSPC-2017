a, d = [int(a) for a in input().split(" ")]
up = [[int(c) for c in input().split(" ")] for _ in range(a)]
down = [[int(c) for c in input().split(" ")] for _ in range(d)]
H = sum([c[0] for c in up])
upH = [[0, 0]]
upT = [0]
for i in range(len(up)):
    sT = upT[i] + up[i][1]
    upH.append([upH[i][0] + up[i][0], sT])
    upT.append(sT)
downH = [[H, 0]]
downT = [0]
for i in range(len(down)):
    sT = downT[i] + down[i][1]
    downH.append([downH[i][0] - down[i][0], sT])
    downT.append(sT)

t = sorted(set(upT + downT))

startA = 0
lUH = len(upH) - 1
def cAH(time):
    global startA
    for i in range(startA, lUH):
        if upH[i + 1][1] > time:
            startA = i
            base = upH[i][0]
            diffH = upH[i+1][0] - upH[i][0]
            diffT = upH[i+1][1] - upH[i][1]
            v = diffH / diffT
            return base + v * (time - upH[i][1])
    return H

startD = 0
lDH = len(downH) - 1
def cDH(time):
    if time >= downH[lDH][1]: return 0
    global startD
    for i in range(startD, lDH):
        if downH[i + 1][1] > time:
            startD = i
            base = downH[i][0]
            diffH = downH[i+1][0] - downH[i][0]
            diffT = downH[i+1][1] - downH[i][1]
            v = diffH / diffT
            return base + v * (time - downH[i][1])
    return 0


uH = [cAH(time) for time in t]
dH = [cDH(time) for time in t]
i = 0
while i < len(t):
    if uH[i] == dH[i]:
        print(t[i])
        exit(0)
    elif uH[i] > dH[i]:
        base = t[i-1]
        time = t[i] - base
        a = dH[i-1]
        b = dH[i]
        c = uH[i - 1]
        d = uH[i]
        e = a-c
        print(time * e/(d-b+e) + base)
        exit(0)
    i += 1
