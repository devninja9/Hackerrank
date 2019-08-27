# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    lines = []
    for i in range(0, 2):
        line = input()
        if line:
            lines.append(line)
        else:
            break

    s1 = lines[0]
    n1 = len(s1)
    s2 = lines[1]
    n2 = len(s2)

    lcs = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1]==s2[j-1]:
                lcs[i][j] = lcs[i-1][j-1]+1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
    print(lcs[-1][-1])