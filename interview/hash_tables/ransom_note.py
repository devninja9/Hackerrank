# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    ran = Counter(note)
    if not ran:
        print("Yes")
        return
    else:        
        for m in magazine:
            if m in ran:
                if ran[m] > 1:
                    ran[m] -= 1
                else:
                    ran.pop(m)
                    if len(ran) == 0:
                        print("Yes")
                        return
    print("No")