import matplotlib.pyplot as plt
import numpy as np
from numpy import diff

N = 30
n = np.arange(0.001, N/2, 1.0/N)
def f(x):
	return np.exp(x)-3*x*x

df = 0.000000000000001
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
	for i in range(1, 30):
		r = -f(a)/(np.exp(a)-6*a)
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
		x = np.exp(x)/6
		print '%3d   %.11f' % (i, x)

		if abs(x-x0) < df :
			break
	print "Sol: ", x


print '\n'
# OK
# Bisection(a, b)
# FalsePosition(a, b)
# Newton(a)
# Secant(a, b)
FixedPoint(b)