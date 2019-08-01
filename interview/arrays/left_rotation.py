# Link
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
    n = len(a) - 1
    if n < d:
        n = d % n
    ret = []
    for i in range(d, n+1):
        ret.append(a[i])
    for i in range(0, d):
        ret.append(a[i])
    return ret