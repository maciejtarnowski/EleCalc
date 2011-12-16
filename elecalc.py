#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from pprint import pprint
from decimal import *
import math

'''
Electronics calculator
(c) Maxik 2011.

TODO:
* Convert just after load, before checking
'''

class Converter(object):
    def __init__(self):
        self.prefixes = {
                        'f': ['femto', 0.000000000000001],
                        'p': ['piko', 0.000000000001],
                        'n': ['nano', 0.000000001],
                        'u': ['micro', 0.000001],
                        'm': ['milli', 0.001],
                        'c': ['centi', 0.01],
                        'd': ['deci', 0.1],
                        'h': ['hecto', 100],
                        'k': ['kilo', 1000],
                        'M': ['mega', 1000000],
                        'G': ['giga', 1000000000],
                        'T': ['tera', 1000000000000],
                        'P': ['peta', 1000000000000000]
                        }
    
    def DetermineFormat(self, amount):
        '''We need to determine format, eg. (10.2k || 10k2) = (False || True)'''
        for char in amount:
            if char.isdigit():
                format = True
            elif char is '.':
                return False
            else:
                format = True
        return True
    
    def ConvertFromMultiplicity(self, amount):
        if self.DetermineFormat(amount):
            result = re.search(r'^([0-9]+)([a-zA-Z])?([0-9])*', amount).groups()
            
            if result[1] is not None:
                pref = result[1]
                try:
                    mult = self.prefixes[result[1]][1]
                except KeyError:
                    mult = 1
            else:
                pref = ''
                mult = 1
            
            if result[2] is not None:
                value = int(result[0])+(int(result[2])*0.1)
            else:
                value = int(result[0])
            
            return value*mult
        else:
            result = re.search(r'^([0-9]+[.]?[0-9]*){1}([fpnumcdhkMGTP])?', amount).groups()
            
            if result[1] is not None:
                pref = result[1]
                try:
                    mult = self.prefixes[result[1]][1]
                except KeyError:
                    mult = 1
            else:
                pref = ''
                mult = 1
            
            value = float(result[0])
            
            return value*mult

class Calculations(object):
    def __init__(self):
        pass
    
    def RCTimeConstant(self):
        pass
    
    def RLTimeConstant(self):
        pass
    
    def RLCTimeConstant(self):
        pass
    
    def RLImpedance(self):
        pass
    
    def RCImpedance(self):
        pass
    
    def RLCImpedance(self):
        pass
    
    def SerialResistor(self, resistors = []):
        if len(resistors) is 0:
            while True:
                n = raw_input('How many resistors are there?: ')
                if n>0:
                    break
            i = 0
            while i<int(n):
                ohm = raw_input('Resistance of %d resistor: ' % (i+1))
                resistors.append(ohm)
                ohm = 0
                i=i+1
        resistance = 0.0
        resistors = map(Converter().ConvertFromMultiplicity, resistors)
        for resistor in resistors:
            resistance+=resistor
        return resistance
    
    def ParallelResistor(self, resistors = []):
        if len(resistors) is 0:
            while True:
                n = raw_input('How many resistors are there?: ')
                if n>0:
                    break
            i = 0
            while i<int(n):
                ohm = raw_input('Resistance of %d resistor: ' % (i+1))
                resistors.append(ohm)
                ohm = 0
                i=i+1
        resistance = 0.0
        resistors = map(Converter().ConvertFromMultiplicity, resistors)
        for resistor in resistors:
            resistance+=(float(1)/float(resistor))
        return (1/resistance)
    
    def SerialCapacitor(self, capacitors = []):
        if len(capacitors) is 0:
            while True:
                n = raw_input('How many capacitors are there?: ')
                if n>0:
                    break
            i = 0
            while i<int(n):
                far = raw_input('Capacity of %d capacitor: ' % (i+1))
                capacitors.append(far)
                far = 0
                i=i+1
        capacity = float(0)
        capacitors = map(Converter().ConvertFromMultiplicity, capacitors)
        for capacitor in capacitors:
            capacity+=float(float(1)/float(capacitor))
        return float(float(1)/capacity)
    
    def ParallelCapacitor(self, capacitors = []):
        if len(capacitors) is 0:
            while True:
                n = raw_input('How many capacitors are there?: ')
                if n>0:
                    break
            i = 0
            while i<int(n):
                far = raw_input('Capacity of %d capacitor: ' % (i+1))
                capacitors.append(far)
                far = 0
                i=i+1
        capacity = 0.0
        capacitors = map(Converter().ConvertFromMultiplicity, capacitors)
        for capacitor in capacitors:
            capacity+=capacitor
        return capacity
    
    def OhmVoltage(self):
        pass
    
    def OhmCurrent(self):
        pass
    
    def OhmResistance(self):
        pass
    
    def CapacitiveReactance(self, frequency = None, capacity = None):
        if ((frequency is None) or (capacity is None)):
            while True:
                frequency = raw_input('Frequency(>0): ')
                if frequency<0:
                    continue
                capacity = raw_input('Capacity(>0): ')
                if capacity<0:
                    continue
                break
        frequency = Converter().ConvertFromMultiplicity(frequency)
        capacity = Converter().ConvertFromMultiplicity(capacity)
        return math.pow((float(2)*math.pi*float(frequency)*float(capacity)), -1)
    
    def InductiveReactance(self):
        pass
    
    def JoulePower(self, amps = None, voltage = None):
        if ((amps is None) or (voltage is None)):
            while True:
                amps = raw_input('Current(>0): ')
                if float(amps)<0:
                    continue
                voltage = raw_input('Voltage: ')
                if float(voltage)<0:
                    voltage = 0-voltage
                break
        amps = Converter().ConvertFromMultiplicity(amps)
        voltage = Converter().ConvertFromMultiplicity(voltage)
        return (amps*voltage)
    
    def TransformerVoltage(self):
        '''We should allow calculation any of the variables supplying the other three'''
        pass


if __name__=='__main__':
    #print '%f Ohms' % Calculations().SerialResistor()
    #print '%f Watts' % Calculations().JoulePower()
    #print '%f Ohms' % Calculations().ParallelResistor()
    #print '%f Farads' % Calculations().SerialCapacitor()
    #print '%f Farads' % Calculations().ParallelCapacitor()
    print '%f Ohms' % Calculations().CapacitiveReactance()
