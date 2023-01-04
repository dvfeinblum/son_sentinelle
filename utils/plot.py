import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt


class Plot:
    def __init__(self, time_step):
        self.x = []
        self.y = []
        self.t = 0
        self.time_step = time_step
        plt.ion()

    def take_step(self, y):
        """
        Adds a new (x,y) point to the plot, re-draws the axes
        and then displays the entire graph.

        :param y:
        :return:
        """
        self.x.append(self.t)
        self.y.append(y)
        plt.gca().cla()
        plt.plot(self.x, self.y)

        plt.draw()
        plt.pause(self.time_step)
        self.t += self.time_step

    def dump_data(self, filename=datetime.now().strftime("output/%Y-%m-%d_%H-%M.csv")):
        """
        Dumps the x/y values in the plot into a file with a fixed name.

        :param filename: name of output file (defaults to yyyy-mm-dd_hh-min.csv)
        """
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for pair in list(zip(self.x, self.y)):
                writer.writerow(pair)
