# use python 3
import sys


def greedy(n, l):
    a, i = 0, 0
    while n != 0:
        b = n // l[i]
        a += b if b > 0 else 0
        n -= b * l[i] if b > 0 else 0
        i += 1
    return a


def dynamic(m, l):
    a = []
    for i in range(m):
        

def canonical(n, l):

    pass


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    canonical(data[0], reversed(data[1:]))
