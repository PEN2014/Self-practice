import matplotlib.pyplot as plt
import numpy as np
from numpy import diff
import math

N = 30
n = np.arange(0.001, N/2, 1.0/N)
def f(x):
	return 2*x*np.cos(2*x)-(x-2)*(x-2)

df = 0.0000000001
a = 2.9
b = 5

def Bisection(a, b):
	for i in range(1, 80):
		c = (a+b)/2
		if f(a)*f(c) < 0 :
			b = c
		else:
			a = c
		print '%3d   %.11f' % (i, c)

		if abs(a-b) < df :
			break
	print "Sol: ", c

def FalsePosition(a, b):
	Xold = a
	for i in range(1, 80):
		Xnew = (a*f(b)-b*f(a))/(f(b)-f(a))
		if f(a)*f(Xnew) < 0 :
			b = Xnew
		else:
			a = Xnew
		print "%3d   %.11f" % (i, Xnew)

		if abs(Xnew-Xold) >= df :
			Xold = Xnew
			continue
		else:
			break
	print "Sol: ", Xnew

def Newton(a):
	for i in range(1, 80):
		r = -(f(a))/( 2*math.cos(2*a)-2*a*math.sin(2*a)-2*a-4 )
		a = a + r
		print "%3d   %.11f" % (i, a)
		if abs(r) < df :
			break
	print "Sol: ", a

def Secant(a, b):
	for i in range(1, 80):
		c = (a*f(b)-b*f(a))/(f(b)-f(a))
		a = b
		b = c
		print '%3d   %.11f' % (i, c)

		if abs(a-b) < df :
			break
	print "Sol: ", c

def FixedPoint(a):
	x = a
	for i in range(1, 20):
		x0 = x
		# x = ( 2*x*(abs(math.cos(2*x)) ))**0.5 + 2
		x = ((x-2)*(x-2))/2*math.cos(2*x)
		# x = (math.acos( ((x-2)*(x-2))/(2*x) ))/2
		print '%3d   %.11f' % (i, x)

		if abs(x-x0) < df :
			break
	print "Sol: ", x

print '\n'
# not yet 3 5
# Bisection(a, b)
# FalsePosition(a, b)
Newton(22)
# Secant(a, b)
# FixedPoint(b)