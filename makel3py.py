# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:42:36 2022

@author: ramazanolcay
"""
import numpy as np
import math

g=9.81
n_tray=20 #number of tray
Fgmin = ((380*540*1.2)*0.0000079) # (N)
Fgmax = (Fgmin + (n_tray*0.61)) # (N)
Psmin = Fgmin * g * 0.5
Psmax = Fgmax * g * 0.5

d = np.arange(0,15) #wire diameter of spring (mm)
C= 9 #spring index 
K = ((4*C - 1)/(4*C - 4)) + (0.615/C) #Stress factor (Wahl Factor)
T = K*((8*Psmax * C)/(math.pi * d * d)) # Torsional shear stress

#Benchmark result in T and give to a spesific value to d
d=2

D = C*d #mean coil diameter (mm)
Di = D - d #inside diameter of spring coil (mm)
Do = D + d #outside diameter of spring coil (mm)

defl= 400 #Deflection
G = 81370 #from table for spring
N = (defl*G*d) / (((Psmax-Psmin))*8*C*C*C) #Number of active coils

N = 187 #Giving a int value for N
defl1 = (8*(Psmax-Psmin)*C*C*C*N)/(G*d) #Correct deflection

Nt = N +2 #total number of coils
soll= Nt*d #solid length
gap = (Nt-1)* 0.5 #total gap
Ltotal = soll + gap + defl1 #free length
pitch = Ltotal / (Nt - 1) # pitch
k_r = (Psmax - Psmin) / defl #spring rate
k_act = (G * d*d*d*d) / (8*D*D*D*N) #actual spring rate