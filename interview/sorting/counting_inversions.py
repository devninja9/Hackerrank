#https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Complete the countInversions function below.
def countInversions(arr):
    n = len(arr)
    if n == 1:
        return arr, 0
    else:
        mid = n // 2
        a = arr[:mid]
        b = arr[mid:]

        a, ai = countInversions(a)
        b, bi = countInversions(b)
        c = []

        i = 0
        j = 0
        inversions = ai + bi
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)
    
    c += a[i:]
    c += b[j:]

    return c, inversions