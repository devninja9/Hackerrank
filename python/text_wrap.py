# https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen
def wrap(string, max_width):    
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])