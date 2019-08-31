# https://www.hackerrank.com/challenges/python-sort-sort/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n, m = map(int, input().split())
    rows = [input() for _ in range(n)]
    k = int(input())

    for row in sorted(rows, key=lambda row: int(row.split()[k])):
        print(row)