'''from __future__ import division'''
from sympy import *
import sys

denklemler = []
yil, x, y, z, t, a, b, c, e, d = symbols('yil, x, y, z, t, a, b, c, e, d')
yil = 0
    
def SetTime(value):
    global yil
    yil = value
def GetTime():
    return yil
    
def AddEq(left, right):
    denklemler.append(Eq(left, right))
    
def SumAges(*items):
    toplam = 0
    for i in items:
        toplam += i.age
    return toplam
      
class person(object):
    def __init__(self, name):
        self.name = name
        self._yas = None
        
    @property 
    def age(self):
        if self._yas is None:
            exec(self.name + 'age = symbols("' + self.name + 'age")')
            return eval(self.name + 'age + yil')
        else:
            return self._yas + yil
    
    @age.setter
    def age(self, value):
        self._yas = value
        AddEq(sympify(self.name + 'age + ' + str(yil)), value)
            
class vehicle(object):
    def __init__(self, name):
        self.name = name
        self._hiz = 0
            
    def Go(self, pyol, deg):
        AddEq(pyol.uzunluk / self._hiz, deg)

    def Go(self, pyol, zaman, deg):
        AddEq(pyol.uzunluk / zaman, deg)
            
    @property 
    def speed(self):
        return self._hiz
    
    @speed.setter
    def speed(self, value):
        self._hiz = value
        AddEq(sympify(self.name + 'hiz'), value)
                   
class way(object):
    def __init__(self, name):
        self.name = name
        self._uzunluk = 0
        
    @property
    def length(self):
        return self._uzunluk
    
    @length.setter
    def length(self, value):
        self._uzunluk = value
        AddEq(sympify(self.name + 'uzunluk'), value)
