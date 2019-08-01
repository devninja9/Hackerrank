# Link
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def hourglassSum(arr):
    max_sum = -9 * 7
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            sum = arr[i-1][j-1] + arr[i+1][j-1] + arr[i-1][j] + arr[i][j] + \
             arr[i+1][j] + arr[i-1][j+1] + arr[i+1][j+1]
            max_sum = max(max_sum, sum)
            
    return max_sum