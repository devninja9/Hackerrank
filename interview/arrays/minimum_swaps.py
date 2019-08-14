#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0    
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] != i+1:
            t = arr[i]
            arr[i] = arr[t-1]
            arr[t-1] = t            
            count += 1
        else:
            i += 1
    return count