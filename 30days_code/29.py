# Problem
# https://www.hackerrank.com/challenges/30-bitwise-and/problem

# Explanation
# a & b = k, b <= a => k <= b
# a & (k-1) <= (k-1)
# if k is odd, k & k-1 = k-1
# if k is even, (k | k-1) & k-1 = k-1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        if k % 2 == 1 or (k | (k -1)) <= n:
            print(k-1)
        else:
            print(k-2)