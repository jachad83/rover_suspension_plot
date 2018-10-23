# Mars Rover Suspension Model
As part of The Open University Rover Challenge Team (http://www.ou-roverteam.co.uk/), I helped develop a Mars rover analogue for entry into the Mars Society University Rover Challenge - http://urc.marssociety.org/.

One of the early stage tasks was to produce a model of how the suspension would behave in order to decide what components and material would be required in production.

I originally completed the task using MatLab; this is a Python port of that task.

## Version
* 1.0.0
* October 2018

The model variables are:

* Deflection distance (produced by weight of the rover and bumps encountered)
* Suspension spring length
* Suspension spring resistance strength / coefficient
* Dampening effect / coefficient
* Point that suspension oscillations are deemed negligible

The model outputs are:

* Time for suspension oscillations to become negligible
* Total number of suspension oscillations before oscillations are deemed negligible

## Dependencies

### Python
* Python 3.6.5
* MatPlotLib 3.0.0
* NumPy 1.15.3

#### Author
* James Chadwick, 2018
