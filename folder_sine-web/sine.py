import matplotlib.pyplot as plt
import numpy as np


# 1
def function1():
	N = 500		# array length
	k = 3		# the frequency
	n = np.arange(-N/2, N/2)	# the time index
	s = np.exp (1j *2 *np.pi *k *n /N)

	plt.plot(n, np.imag(s))		# n and against the real part of s np.real(s)
	plt.axis([-N/2, N/2, -1, 1])
	plt.xlabel('n')
	plt.ylabel('amplitude')
	plt.show()


# 2
def function2():
	A = .8
	f0 = 1000		# Herz
	phi = np.pi/2	# initial phrase
	fs = 44100		# T (sample period) = 1/44100
	t = np.arange (-0.002, .002, 1.0/fs) # vector for the time index, an array
	x = A * np.cos (2 * np.pi * f0 * t + phi)

	plt.plot(t, x)	# time array with respect to the x values
	plt.axis([-.002, .002, -.8, .8])
	plt.xlabel('time')
	plt.ylabel('amplitude')
	plt.show()

function2()