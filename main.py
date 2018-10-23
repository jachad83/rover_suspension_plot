#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np


def wave_calc():
    # derive data
    Fs = 8000
    f = 5
    sample = 8000
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)

    return x, y


def plot():
    # plot data
    x, y = wave_calc()

    plt.plot(x, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()
