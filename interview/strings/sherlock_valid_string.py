# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    s = input()

    n = len(s)
    if n < 4:
        print("YES")
    else:
        count = [0] * 26
        for i in range(0, n):
            c = ord(s[i]) - 97
            count[c] += 1

        a = -1;ac = 0
        b = -1;bc = 0
        fail = False
        for i in range(0, 26):
            if count[i] != 0:
                if a == -1:
                    a = count[i]
                    ac = 1
                else:
                    if count[i] != a:
                        if b == -1:
                            b = count[i]
                            bc = 1
                        else:
                            if count[i] != b:
                                fail = True
                                break        
                            else:
                                bc += 1
                    else:
                        ac += 1

        if fail:
            print("NO")
        else:
            if ac > 1 and bc > 1:
                print("NO")
            else:              
                if ac == 1 and (a == 1 or ((a-b) == 1)):
                    print("YES")
                elif bc == 1 and (b == 1 or (b-a == 1)):
                    print("YES")
                elif bc == 0 or ac == 0:
                    print("YES")
                else:
                    print("NO")