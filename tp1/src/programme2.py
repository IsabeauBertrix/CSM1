#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import methodes
import equations

# Résolution approchée de y' = 1-y avec y(0) = 5 pour t dans [0,1]
equations.a = -1.
equations.b = 1.
equations.c = 2
t0,y0 = 0.,2.
i=0
# Avec un pas de 0.2, il faut donc 5 iterations
N,h = 5,0.2
plt.xlabel('t')
plt.ylabel('y')
plt.title("Erreurs")
plt.legend()
N= 5
h=0.2
for i in range (5) :
	[t,y1] = methodes.euler_explicite(t0,h,N,y0,equations.f_affine2)
	# Solution exacte aux mêmes instants
	z1 = equations.sol_affine2(t,y0)
	# tableau erreur
	erreur = np.abs(z1-y1)
	# Graphe des solutions exactes et approchées
	plt.plot(t,np.exp(erreur))
	print("{0} | {1}".format(h,erreur))
	N=2*N
	h=h/2
plt.show()


