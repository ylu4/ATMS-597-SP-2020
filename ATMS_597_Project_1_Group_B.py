""" 
  This module includes
  inter-conversion between "Celsius",
  "Fahrenheit" and "Kelvin".
  
  Input datatype includes list and array.
"""
__author__      = "Piyush Garg, Dongwei Fu and Bowen Fang"
__copyright__   = "Copyright 2020, ATMS-597 Group B"

import numpy as np
import scipy as sp
import math 

class tempconvert: 

  
  # Conversion Attributes
  def __init__(self, scale, temp):
  """
  Create the conversion object with 2 arguments
  Args:
        param1: scale (unit) of the temperature values. (string)
        param2: input temperature values. (int./float.)
  
  Input Datatype:
        list;
        array;
  """
      self.temp = temp       
      self.scale = scale     
  
  #Conversion to Celsius method
  def Celsius(self):
  """
  Function of converting temperature inputs to Celsius

  Return: Celsius temperature values
  
  Datatype: same as input (array, list)
  """

    temp_conv = np.zeros((np.shape(self.temp)))    
    if self.scale == 'F':
      for i in range(len(self.temp)):
        temp_conv[i] = (self.temp[i] - 32.) * (5/9)
    if self.scale == 'K':
      for i in range(len(self.temp)):
        temp_conv[i] = (self.temp[i] - 273.15)
    if type(self.temp)==list:
      return temp_conv.tolist()
    else:
      return temp_conv
  
  #Conversion to Fahrenheit method
  def Fahrenheit(self):
  """
  Function of converting temperature inputs to Fahrenheit

  Return: Fahrenheit temperature values
  
  Datatype: same as input (array, list)
  """

    temp_conv = np.zeros((np.shape(self.temp)))
    if self.scale == 'C':
      for i in range(len(self.temp)):
        temp_conv[i] = ((self.temp[i]) * (9/5)) + 32.
    if self.scale == 'K':
      for i in range(len(self.temp)):
        temp_conv[i] = ((self.temp[i]) * (9/5)) - 459.67
    if type(self.temp)==list:
      return temp_conv.tolist()
    else:
      return temp_conv

  #Conversion to Kelvin method
  def Kelvin(self):
  """
  Function of converting temperature inputs to Kelvin

  Return: Kelvin temperature values
  
  Datatype: same as input (array, list)
  """
  
    temp_conv = np.zeros((np.shape(self.temp)))
    if self.scale == 'C':
      for i in range(len(self.temp)):
        temp_conv[i] = (self.temp[i] + 273.15)
    if self.scale == 'F':
      for i in range(len(self.temp)):
        temp_conv[i] = (self.temp[i] + 459.67) * (5/9)
    if type(self.temp)==list:
      return temp_conv.tolist()
    else:
      return temp_conv