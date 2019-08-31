# https://www.hackerrank.com/challenges/any-or-all/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n,m = int(input()), input().split()
    print(all([int(i) > 0 for i in m]) and any([i == i[::-1] for i in m]))