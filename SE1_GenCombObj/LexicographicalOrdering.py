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
            if xt == 1:
                t.append(self.X[counter])
            counter += 1

        return t