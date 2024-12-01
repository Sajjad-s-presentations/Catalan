class Permutation:
    def __init__(self, m):
        print("Permutation constructor is called with order {}".format(m))
        self.m = m
        self.partition = []

    def generate_parrtitions(self, curr_m, B, N):
        print(curr_m)
        if curr_m == 0:
            return self.partition
        else:
            for i in range(1, min(B, curr_m)):
                self.partition.append(i)
                self.generate_parrtitions(curr_m-i, i, N+1)
