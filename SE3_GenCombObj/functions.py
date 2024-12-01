class Permutation:
    def __init__(self, m):
        print("Permutation constructor is called with order {}".format(m))
        self.m = m
        self.partition = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def generate_parrtitions(self, curr_m, B, N):
        if curr_m == 0:
            return self.partition
        else:
            for i in range(1, min(B, curr_m)):
                self.partition[N+1] = i
                self.generate_parrtitions(curr_m-i, i, N+1)


    def ferres_ypung_diagram(self, arr):
        for a in arr:
            for i in range (0, a):
                print("*", end="")
            print("")
