import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#prepare data
machine_types = [18,4,2]

#prepare labels
machine_names =["PC","MAC","Linux"]

#Draw pie
pyplot.pie(machine_types, labels= machine_names)

#show
pyplot.show()
