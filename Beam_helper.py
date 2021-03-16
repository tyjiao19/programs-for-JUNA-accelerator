#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# tyjiao @ 2021-03-16 00:02:48

import math as m

#He++
M = 4
q = 2

E_ion_source = 40 #kV
E_acc = 350 #kV
E = E_ion_source + E_acc

G1 = 320
G2 = 183
D1 = 100.4

D2 = 64.785
Q1 = 21.7
Q2 = 5.6
Q3 = 75.3
Q4 = 29.8

Br = m.sqrt(2*M*E)/q

def Ion(mode,par,E_ion,old_E):
    result = par*mode*m.sqrt(E_ion/old_E)/2
    return result

def Acc(mode,par,E,old_E):
    result = par*mode*m.sqrt(E/old_E)/2
    return result

def select_mode():
    print("please input the tybe of beam (with number):")
    print("1> H+    2> He+    3> He++")
    while True:
        select = input()
        if select == 1 :
            return 2;
        if select == 2 :
            return 8;
        if select == 3 :
            return 4;
        else: 
            print("Sorry,syntax error.")

mode = m.sqrt(select_mode())
Ideal_E_ion = input('please input the expected E_ion_source(kV) : ')
Ideal_E_acc = input('please input the expected E_acc(kV) : ')
Ideal_E = Ideal_E_ion+Ideal_E_acc
print('magnetic rigidity = %.3f'%Br)
G1_n = Ion(mode,G1,Ideal_E_ion,E_ion_source)
G2_n = Ion(mode,G2,Ideal_E_ion,E_ion_source)
D1_n = Ion(mode,D1,Ideal_E_ion,E_ion_source)
print('G1 = %.1f'%G1_n,'G2 = %.1f'%G2_n,'D1 = %.1f'%D1_n)
D2_n = Acc(mode,D2,Ideal_E,E)
Q1_n = Acc(mode,Q1,Ideal_E,E)
Q2_n = Acc(mode,Q2,Ideal_E,E)
Q3_n = Acc(mode,Q3,Ideal_E,E)
Q4_n = Acc(mode,Q4,Ideal_E,E)
print('D2 = %.3f'%D2_n,' Q1 = %.1f'%Q1_n,' Q2 = %.1f'%Q2_n,' Q3 = %.1f'%Q3_n,' Q4 = %.1f'%Q4_n)

