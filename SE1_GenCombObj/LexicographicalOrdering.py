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

    def getXTbyT(self, T):
        xt = []
        counter = 0
        n = len(self.X)+1
        for t in self.X:
            if int(t) in T:
                xt.append('1')
            else:
                xt.append('0')
            counter += 1

        return xt


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
        X_len = range(len(self.X)+1)
        for i in reversed(X_len):
            if i == 0:
                break
            if r % 2 == 1.0:
                T.append(i)
            r = r/2

        return T

    def SubsetLexSuccessor(self, T):
        n = len(self.X)
        for i in range(n):
            if n-i in T:
                T.remove(n-i)
            else:
                break

            if i <= n-1:
                T.append(n-i)
        return T
