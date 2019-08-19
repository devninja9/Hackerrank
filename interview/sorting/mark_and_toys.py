#https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    sum = 0
    count = 0
    for i in range(0, len(prices)):
        sum += prices[i]
        if sum <= k:
            count += 1
        else:
            break
    return count