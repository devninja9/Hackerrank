#https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0] * n
    for i in range(0, len(queries)):
        query = queries[i]
        a = query[0]
        b = query[1]
        k = query[2]

        array[a-1] += k
        if b < n:
            array[b] -= k

    val = array[0]
    maximum = val
    for i in range(1, n):
        val += array[i]
        maximum = max(maximum, val)

    return maximum