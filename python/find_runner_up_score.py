if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(sorted(set(arr), reverse=True))
    print(arr[1])