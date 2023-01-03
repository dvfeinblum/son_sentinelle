import matplotlib.pyplot as plt
from math import inf

class Plot:
    def __init__(self, time_step, t_max=inf):
        self.x = []
        self.y = []
        self.t = 0
        self.time_step = time_step
        self.t_max = t_max
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

    @property
    def can_step(self):
        return self.t < self.t_max
