#https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    q = int(input())

    for i in range(0, q):
        s = input()
        if len(s) < 2:
            print(0)
        else:
            count = 0
            current = s[0]
            for j in range(1, len(s)):
                if s[j] == current:
                    count += 1
                else:
                    current = s[j]
            print(count)
