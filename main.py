#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import math


# model variables
MIN_DEFLECTION = 0.01  # in m
SAMPLE_RATE = 0.01  # in s
SAMPLE_TIME = 5  # in s


def wave_calc(deflection, mass, spring_constant, damping_coefficent):
    # angular frequency
    w = math.sqrt(spring_constant / mass)
    print(f'Spring period of oscillation {math.sqrt(mass / (spring_constant*1000))*(2 * math.pi)} s.')

    # numpy arrays for x and y coords
    x = np.arange(0, SAMPLE_TIME, SAMPLE_RATE)
    y = np.arange(0, SAMPLE_TIME, SAMPLE_RATE)

    # iterate over y array
    with np.nditer(y, op_flags=['readwrite']) as arr:
        for el in arr:
            # under-damped harmonic oscillator equation
            el[...] = deflection * math.exp(-el*damping_coefficent) * math.cos(2 * math.pi * el)

    return wave_plot(x, y)


def wave_plot(x, y):
    # plot data
    plt.plot(x, y)
    plt.title('Rover Suspension Displacement')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.grid(True, which='both')
    plt.show()


def main():
    # user inputs
    INITIAL_DEFLECTION = float(input('Initial deflection in m: '))
    MASS = float(input('Mass in kg: '))
    SPRING_CONSTANT = float(input('Spring constant in kiloNewtons per metre: '))
    DAMPING_COEFFICIENT = float(input('Damping coefficient (unit-less): '))
    wave_calc(deflection=INITIAL_DEFLECTION, mass=MASS, spring_constant=SPRING_CONSTANT, damping_coefficent=DAMPING_COEFFICIENT)


if __name__ == "__main__":
    main()
