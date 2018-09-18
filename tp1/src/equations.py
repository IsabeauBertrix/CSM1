#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

# Fonction f(t,y), second membre d'équations différentielles d'ordre 1
# écrite sous la forme d'un problème de Cauchy, y'(t) = f(t,y(t)) avec
# y(0)=y0

a = -1.
b = 1.
c = 2

def f_affine(t,y):
    """Fonction affine pour y' = ay+b. Les coefficients a et b sont des
    variables globales du module.

    """
    return a*y+b

def f_affine2(t,y):
    return a * math.pow( y , c ) + b

def sol_affine(t,y0):
    """Pour une fonction affine, on connait la solution exacte. C'est
    y(t0+s) = y0*exp(a*s) - b*(1-exp(a*s))/a, soit y(t) =
    y0*exp(a*(t-t0)) - b*(1-exp(a*(t-t0)))/a

    """
    t0 = t[0]
    return y0*np.exp(a*(t-t0)) - b * (1.-np.exp(a*(t-t0)))/a

def sol_affine2(t,y0):
    
    if y0 < -1 :
        k =  - 2 * t + np.log(( -y0 - 1 ) / ( 1 - y0 ))
        return (np.exp( 2 * t + k ) + 1 ) / ( np.exp( 2 * t + k ) - 1 )
    if -1 < y0 < 1 :
        k =  - 2 * t + np.log(( 1 + y0 ) / ( 1 - y0 ))
        return (np.exp( 2 * t + k ) - 1 ) / ( np.exp( 2 * t + k ) + 1 )
    if 1 < y0 :
        k = -  2 * t + np.log(( 1 + y0 ) / ( y0 - 1 ))
        return ( -1 - np.exp( 2 * t + k) ) / ( 1 - np.exp( 2 * t +k ) )
    

