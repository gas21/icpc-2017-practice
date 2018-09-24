# use python 3
import sys
from operator import itemgetter


def greedy(n, l):
    l = l[::-1]
    a, i = 0, 0
    while n != 0:
        b = n // l[i]
        a += b if b > 0 else 0
        n -= b * l[i] if b > 0 else 0
        i += 1
    return a


def dynamic(m, l):
    sol, b = [1], len(l)
    for change in range(2, m + 1):
        b = len(l)
        while True:
            if change in l:
                sol.append(1)
                break
            else:
                try:
                    s = min([sol[change - x - 1] for x in l[:b]])
                    sol.append(s + 1)
                    break
                except IndexError:
                    b -= 1
    return sol[-1]


def canonical(n, l):
    j = l[-1] + l[-2]
    for i in range(1, j):
        a, b = dynamic(i, l), greedy(i, l)
        if a != b:
            print("non-canonical")
            return
    print("canonical")


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    canonical(data[0], data[1:])
