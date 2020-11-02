import sys

def stitch(silL, silR):
    hold = []
    sil = []
    hold.append(0)
    i = 0
    j = 0
    leftWasPrev = False
    while i < len(silL) and j < len(silR):
        if silL[i][0] == silR[j][0]:
            if silL[i][1] > silR[j][1]:
                sil.append(silL[i])
                hold.append(silL[i][1])
                leftWasPrev = True
                i += 1
            elif silL[i][1] < silR[j][1]:
                sil.append(silR[j])
                hold.append(silR[j][1])
                leftWasPrev = False
                j += 1
            else:
                sil.append(silL[i])
                hold.append(silL[i][1])
                leftWasPrev = True
                i += 1
                j += 1

        elif silL[i][0] < silR[j][0]:
            if silL[i][1] > hold[-1]:
                if (leftWasPrev):
                    hold.pop()
                sil.append(silL[i])
                hold.append(silL[i][1])
                leftWasPrev = True
            elif silL[i][1] == hold[-1]:
                leftWasPrev = True
            elif leftWasPrev:
                hold.pop()
                if j == 0:
                    sil.append(silL[i])
                    hold.append(silL[i][1])
                else:
                    sil.append((silL[i][0], hold[-1]))
                    hold.insert(-1, silL[i][1])
                    leftWasPrev = False
            else:
                hold.insert(-1, silL[i][1])
            i += 1

        else:
            if silR[j][1] > hold[-1]:
                if (not leftWasPrev):
                    hold.pop()
                sil.append(silR[j])
                hold.append(silR[j][1])
                leftWasPrev = False
            elif silR[j][1] == hold[-1]:
                leftWasPrev = False
            elif not leftWasPrev:
                hold.pop()
                if silR[j][1] > hold[-1]:
                    sil.append(silR[j])
                    hold.append(silR[j][1])
                else:
                    sil.append((silR[j][0], hold[-1]))
                    hold.insert(-1, silR[j][1])
                    leftWasPrev = True
            else:
                hold.insert(-1, silR[j][1])
            j += 1

    if i < len(silL):
        sil.extend(silL[i:])
    else:
        sil.extend(silR[j:])
    if sil[-1] == sil[-2]:
        sil.pop()
    return sil

def silhouette(s):
    if len(s) > 1:
        sl = s[:len(s)//2]
        sr = s[len(s)//2:]
        silL = silhouette(sl)
        silR = silhouette(sr)
        sil = stitch(silL, silR)
    else:
        sil = []
        s = s[0]
        sil.append((s[0], s[1]))
        sil.append((s[2], 0))
    if len(s) == 0:
        return
    return sil


file = sys.argv[-1]
f = open(file, 'r')
s = f.readline().strip()
while (s != "#hw2_4b"):
    s = f.readline().strip()
squares = f.readline().strip()
squares = squares.replace('[', '')
squares = squares.replace('(', '')
squares = squares.replace(')', '')
squares = squares.replace(']', '')
squares = squares.replace(' ', '')
squares = squares.split(',')

s = []
i = 0

while i < len(squares):
    tempTup = (int(squares[i]), int(squares[i+1]), int(squares[i+2]))
    s.append(tempTup)
    i += 3

s.sort()
print(silhouette(s))
