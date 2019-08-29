# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    ret = "NO"
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    for i in range(0, 26):
        ch = chr(i+97)
        if ch in c1 and ch in c2:
            ret = "YES"
            break
    return ret