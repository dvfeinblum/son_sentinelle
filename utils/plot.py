import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt
from math import inf

class Plot:
    def __init__(self, time_step):
        self.x = []
        self.y = []
        self.t = 0
        self.time_step = time_step
        plt.ion()

    def take_step(self, y):
        self.x.append(self.t)
        self.y.append(y)
        plt.gca().cla()
        plt.plot(self.x, self.y)

        plt.draw()
        plt.pause(self.time_step)
        self.t += self.time_step

    @staticmethod
    def show(**kwargs):
        plt.show(**kwargs)

    def dump_data(self, filename=datetime.now().strftime("output/%Y-%m-%d_%H-%M.csv")):
        """
        Dumps the x/y values in the plot into a file with a fixed name.

        :return: None
        """
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for pair in list(zip(self.x, self.y)):
                writer.writerow(pair)
