class LexographicalOrdering:
    def __init__(self, n):
        print("Lexicographical Ordering")
        self.X = []
        for i in range(1, n+1):
            self.X.append(i)

    def get_X(self):
        return self.X