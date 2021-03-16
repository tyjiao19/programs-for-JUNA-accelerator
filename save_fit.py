#!/usr/bin/python
# -*- coding: utf-8 -*-
# tyjiao @ 2020-12-20 23:31:47

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
############################################

E = [375,330,210]
Q1 = [30.9,30.1,24.9]
Q2 = [20.1,19.8,14.5]
Q3 = [37,34.5,31.5]
Q4 = [19,17.9,13.8]
D2 = [44.7,42.4,33.83]

############################################
def func(x, a):
    return a * x**(0.5)

def draw_fit(x,y1):
    popt, pcov = curve_fit(func, x, y1)

    yy = [func(i,popt[0]) for i in h]

    print ( popt[0])
    return yy


x = np.array(E)
y1 = np.array(Q1)
y2 = np.array(Q2)
y3 = np.array(Q3)
y4 = np.array(Q4)
y5 = np.array(D2)

plot1 = plt.plot(x, y1, 'ks',label='orig1')
plot2 = plt.plot(x, y2, 'ks',label='orig2') 
plot3 = plt.plot(x, y3, 'ks',label='orig3')
plot4 = plt.plot(x, y4, 'ks',label='orig4')
plot5 = plt.plot(x, y5, 'ks',label='orig5') 

h = np.arange(0, 400, 1)

yy1=draw_fit(x,y1)
yy2=draw_fit(x,y2)
yy3=draw_fit(x,y3)
yy4=draw_fit(x,y4)
yy5=draw_fit(x,y5)

plt.plot(h, yy1, 'r-', linestyle='--',label='I_Q1')
plt.plot(h, yy2, 'b-', linestyle='--',label='I_Q2')
plt.plot(h, yy3, 'g-', linestyle='--',label='II_Q1')
plt.plot(h, yy4, 'y-', linestyle='--',label='II_Q2')
plt.plot(h, yy4, 'c-',linestyle='--',label='II_Dipole')

plt.grid()
plt.xlabel('Energy')
plt.ylabel('Q_cur')
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.title('E-Q')
plt.subplots_adjust(right=0.75)

plt.xlim(0,400)
plt.ylim(0,50)

plt.show()
