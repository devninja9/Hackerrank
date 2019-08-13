# Link
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    b = q
    
    count = 0
    for i in range(n-1, -1, -1):
        if b[i] != i+1:
            if i-1 >= 0 and b[i-1] == i+1:
                count = count + 1
                t = b[i-1]
                b[i-1] = b[i]
                b[i] = t
            elif i-2 >=0 and b[i-2] == i+1:
                count = count + 2
                t = b[i-2]
                b[i-2] = b[i-1]
                b[i-1] = b[i]
                b[i] = t
            else:
                count = 'Too chaotic'
                break
    print(count)