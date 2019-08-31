# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    n = int(input())
    scoresheet = [[input(), float(input())] for _ in range(n)]
    second_highest = sorted(list(set([marks for name, marks in scoresheet])))[1]
    print('\n'.join([a for a, b in sorted(scoresheet) if b == second_highest]))