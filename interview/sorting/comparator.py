#https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        print(self.name, self.score)        
    def comparator(a, b):
        if a.score == b.score:
            if a.name == b.name: return 0
            if a.name > b.name: return 1
            else: return -1
        return b.score - a.score   