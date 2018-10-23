#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


# model variables
INITIAL_DEFLECTION = 0.1  # in m
MASS = 100  # in kg
SPRING_LENGTH = 0.3  # in m
SPRING_CONSTANT = 0.3
DAMPENING = 0.3
MIN_DEFLECTION = 0.01  # in m
SAMPLE_RATE = 1000  # in ms


def wave_calc():
    # derive data
    period = 0.01  # testing only
    x = np.arange(SAMPLE_RATE)
    y = np.cos((x * period)) * 0.1

    return x, y


def plot():
    # plot data
    x, y = wave_calc()
    plt.plot(x, y)
    plt.xlabel('Time (ms)')
    plt.ylabel('Displacement (m)')
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()
