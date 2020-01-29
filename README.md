# ATMS-597 Project 1 Group B documentation

This is the README documentation for Group B Project 1 python script.

Copyright ATMS 587 Group B: Piyush Garg, Dongwei Fu and Bowen Fang

Function: This script converts temperatures between "Celsius", "Fahrenheit" and "Kelvin".

Datatype: This script works with list, array and single value inputs.

Return: This script outputs the temperature values in the selected unit and the same datatype as the input.

Usage: example: var1 = tempconvert("K",temp1) var1 is the object that you wish to store the temperature conversion, the 1st argument on the right hand side ("K", or "C" or "F") is the unit of the input values (which accepts string datatype), while the 2nd argument (temp1) is the actual input value (which accept int., float. datatype). In this case, the input temperature are in "Kelvin"(s)

to convert kelvin to celsius: var1.celsius() to convert kelvin to fahrenheit: var1.fahrenheit()

Example input and output:
input command: con_k = tempconvert("K",np.arange(280.,320.,5.))
convert commend: con_k.Fahrenheit()
output: array([ 44.33,  53.33,  62.33,  71.33,  80.33,  89.33,  98.33, 107.33])


Limitation: With selected input unit, the output cannot be of the same unit.

