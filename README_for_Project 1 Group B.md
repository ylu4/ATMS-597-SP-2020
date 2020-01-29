#documentation for Project 1 Group B python script

Copyright ATMS 587 Group B: Piyush Garg, Dongwei Fu and Bowen Fang

Function: 
This script converts temperatures between "Celsius",
"Fahrenheit" and "Kelvin".

Datatype: This script works with list, array and single value inputs.

Return: This script outputs the temperature values in the selected unit
and the same datatype as the input.

Usage: 
example: var1 = tempconvert("K",temp1)
var1 is the object that you wish to store the temperature conversion,
the 1st argument on the right hand side ("K", or "C" or "F") is the
unit of the input values, while the 2nd argument (temp1) is the actual 
input value. In this case, the input temperature are in "Kelvin"(s)

to convert kelvin to celsius:
var1.celsius() 
to convert kelvin to fahrenheit:
var1.fahrenheit()

Limitation:
With selected input unit, the output cannot be of the same unit.
