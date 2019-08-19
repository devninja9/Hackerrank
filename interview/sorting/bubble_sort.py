#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                t = a[j]
                a[j] = a[i]
                a[i] = t
                count += 1
    print("Array is sorted in %d swaps."%(count))
    print("First Element: %d"%(a[0]))
    print("Last Element: %d"%(a[n-1]))