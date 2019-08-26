# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the substrCount function below.
def substrCount(n, s):
    counter = []
    ch = s[0]
    count = 1
    j = 0
    for c in s[1:]:
        if c == ch:
            count += 1
        else:
            counter.append((ch, count))
            ch = c
            count = 1
    counter.append((ch, count))

    result = 0
    for ch,c in counter:
        result += c * (c+1)//2
    for i in range(1, len(counter)-1):
        if counter[i][1] == 1 and counter[i-1][0] == counter[i+1][0]:
            result += min(counter[i-1][1], counter[i+1][1])

    return result