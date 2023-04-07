from p import make_PNG
from math import sin


def merge(c1, c2, ws):
    return tuple(map(int, ((_1 * w + _2 * (1 - w)) % 256
                           for _1, _2, w in zip(c1, c2, ws))))

def makew(r, c):
    return (sin(r * c),
            sin(r * c),
            sin(r * c))

MAG = 255, 0, 255
CYA = 0, 255, 255

ws = 100
hs = 100

w = 1920
h = 1080

arr = [
    merge(MAG, CYA, makew(r, c))
    for r in range(h)
    for c in range(w)
]

make_PNG(arr, w, h, 'back.png')
