# Comp-Inst-Thermistor
A project I made for my Computerized Instrumentation class. 

## Thermistor
The Thermistor Code is specifically crafted to work with an ESP32. The resistance of a thermistor is measured, and this controls the heater which heats said thermistor.
A target resistance is inputted at the beginning of every run. 
You will have to either change the pinouts or set up everything specifically. 
Do NOT use the ESP32's 5V output for the heater.
Make sure to use a transistor and/or HEXFET to control input/output signals.

## Best Fit Program
You will have to manually input values into the program. "Resistances" is meant to be an X-Axis and "Temperatures" is meant to be a Y-Axis.
Once inputted, the program will give two coefficients, A and B. These are meant to be the coefficients for Y = Ax + B, the line of best fit for the inputted data.
