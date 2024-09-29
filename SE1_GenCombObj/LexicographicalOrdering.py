import math


class LexographicalOrdering:
    def __init__(self, n):
        print("Lexicographical Ordering")
        self.X = []
        self.T = []
        for i in range(1, n+1):
            self.X.append(i)

    def get_X(self):
        return self.X

    def getTbyXT(self, XT):
        t = []
        counter = 0
        for xt in XT:
            if xt == '1':
                t.append(self.X[counter])
            counter += 1
        return t

    def LexoTable(self):
        X_len = len(self.X)
        for i in range((X_len*X_len)-1):
            curr_xt = bin(i)[2:].zfill(X_len)
            xt = [x for x in curr_xt]
            print("Rank: {} X(T): {} T: {}".format(i, xt, self.getTbyXT(xt)))


    def SbsetLexRank(self, T):
        r = 0
        X_len = len(self.X)
        for i in range(1, X_len+1):
            if i in T:
                r = r + math.pow(2, (X_len-i))

        return r

    def SbsetLexUnrank(self, r):
        T = []
        X_len = len(self.X)
        for i in range( X_len +1, 1):
            print(i)
