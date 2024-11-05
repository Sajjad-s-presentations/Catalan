import matplotlib.pyplot as plt
class Catalan:
    def __init__(self):
        print("Catalan is called!")


    def sequence_to_path(self, sequence):
        X = [0]
        Y = [0]
        currX = 0
        currY = 0
        for s in sequence:
            if s == '0':
                currY += 1
            else:
                currY -= 1
            currX += 1
            X.append(currX)
            Y.append(currY)

        plt.plot(Y, linestyle='dotted')
        plt.show()
        #return(X, Y)
