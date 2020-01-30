# ATMS-597 Project 1 Group B documentation

This is the README documentation for Group B Project 1 python script.

Copyright ATMS 587 Group B: Piyush Garg, Dongwei Fu and Bowen Fang

Function: This script converts temperatures between "Celsius", "Fahrenheit" and "Kelvin".

Datatype: This script works with list, array and single value inputs.

Return: This script outputs the temperature values in the selected unit and the same datatype as the input.

Usage: example: var1 = tempconvert("K",temp1)
var1 is the object that you wish to store the temperature conversion, the 1st argument on the right hand side ("K", or "C" or "F") is the scale (unit) of the input temperature values (which accepts string datatype), while the 2nd argument (temp1) is the actual input value (which accept int., float. datatype). In this case, the input temperature are in "Kelvin"(s)

to convert from Kelvin to Celsius: var1.celsius() to convert from Kelvin to Fahrenheit: var1.fahrenheit()

Example inputs and outputs:
(array example)
input command: con_k = tempconvert("K",np.arange(280.,320.,5.))
convert command: con_k.Fahrenheit()
output: array([ 44.33,  53.33,  62.33,  71.33,  80.33,  89.33,  98.33, 107.33])

(list example)
con_f = tempconvert("F",np.arange(72.,85.,1.).tolist())
convert command: con_f.Celsius()
output: [22.22222222222222, 22.77777777777778, 23.333333333333336, 23.88888888888889, 24.444444444444446, 25.0, 25.555555555555557, 26.11111111111111, 26.666666666666668, 27.222222222222225, 27.77777777777778, 28.333333333333336, 28.88888888888889]


Limitation: With selected input unit, the output cannot be of the same unit.
