# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    sub_string_len = len(sub_string)
    count = 0
    for i in range(0, len(string) - sub_string_len + 1):
        if sub_string == string[i:i+sub_string_len]:
            count += 1
    return count