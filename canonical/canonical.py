# use python 3
import sys


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
    sol = [1]
    b, mj = len(l), 0
    for change in range(2, m + 1):
        if change in l:
            sol.append(1)
            yield 1
        else:
            while l[mj] < change and mj < b-1:
                mj += 1
            s = min([sol[change - x - 1] for x in l[:mj]])
            sol.append(s + 1)
            yield s + 1


def canonical(l):
    j = l[-1] + l[-2] - 1
    z = dynamic(j, l)
    for a, i in zip(z, range(2, j)):
        if a != greedy(i, l):
            print("non-canonical")
            return
    print("canonical")


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    canonical(data[1:])
