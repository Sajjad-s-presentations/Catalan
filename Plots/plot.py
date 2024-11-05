import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        print("Plot is called")

    def line_only_y_plot(self, y):
        plt.plot(y, linestyle='dotted')
        plt.show()