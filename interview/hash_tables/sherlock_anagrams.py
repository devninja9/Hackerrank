# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    dic = dict()
    for length in range(1, len(s)):
        for start in range(len(s)-length+1):
            sub = ''.join(sorted(s[start:start+length]))
            if sub in dic:
                dic[sub] += 1
            else:
                dic[sub] = 1
    count = 0
    for v in dic.values():
        count += v*(v-1)//2
    return count