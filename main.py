from SE1_GenCombObj.LexicographicalOrdering import LexographicalOrdering
from Catalans.catalans import Catalan
from Plots.plot import Plot

C1 = Catalan()
P1 = Plot()
path = C1.sequence_to_path('0010011010011011')
print(path)
P1.line_only_y_plot(path[1])



