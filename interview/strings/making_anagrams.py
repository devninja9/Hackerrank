#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    counter = [0] * 26
    
    la = len(a)
    lb = len(b)
    for i in range(0, la):
        asc = ord(a[i]) - 97
        counter[asc] += 1
    for i in range(0, lb):
        asc = ord(b[i]) - 97
        counter[asc] -= 1

    count = 0
    for i in range(0, 26):
        count += abs(counter[i])
    
    return count