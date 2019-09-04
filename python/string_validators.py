# https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))