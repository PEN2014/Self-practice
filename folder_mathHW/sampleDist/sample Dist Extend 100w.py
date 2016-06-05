import numpy.numarray as na
from pylab import *
import random

height = []
weight = []
num_height = []
for x in range(1000000):
	height.append(random.randint(140, 185)) # array[46]
	weight.append(random.randint(50, 132))
def COUNT1():
	for x in range(185):		# init counting
		num_height.append(0)
	for x in height:			# counting
		num_height[x-1] +=  1

def PIC1():
	location = na.array(range(185))
	b1 = bar(location, num_height, width=0.6, color='c')
	xticks(range(140, 190, 5))
	yticks(range(0, 50000, 1000))
	xlim(135, 190)
	ylim(0, 10000)
	xlabel('Height', fontsize=12)
	ylabel('The number of each Height', fontsize=12)
	show()
'''====================================================='''
height_ave__05 = []
num_ave__05 = []
for x in range(0, len(height), 5):
	height_ave__05.append(sum(height[x:x+5])/5)

def COUNT2():
	for x in range(185):
		num_ave1.append(0)
	for x in height_ave1:
		num_ave1[x-1] += 1

def PIC2():
	location = na.array(range(185))
	b1 = bar(location, num_ave1, width=0.6, color='c')
	xticks(range(140, 190, 5))
	yticks(range(0, 50000, 1000))
	xlim(135, 190)
	ylim(0, 10000)
	show()
'''====================================================='''
height_ave__10 = []
num_ave__10 = []
for x in range(0, len(height), 10):
	height_ave__10.append(sum(height[x:x+10])/10)

height_ave__25 = []
num_ave__25 = []
for x in range(0, len(height), 25):
	height_ave__25.append(sum(height[x:x+25])/25)

height_ave__50 = []
num_ave__50 = []
for x in range(0, len(height), 50):
	height_ave__50.append(sum(height[x:x+50])/50)

height_ave__100 = []
num_ave__100 = []
for x in range(0, len(height), 100):
	height_ave__100.append(sum(height[x:x+100])/100)

height_ave__500 = []
num_ave__500 = []
for x in range(0, len(height), 500):
	height_ave__500.append(sum(height[x:x+500])/500)

'''====================================================='''
def COUNT(NUM, SAMPLE):
	for x in range(185):
		NUM.append(0)
	for x in SAMPLE:
		NUM[x-1] += 1
def PIC(NUM):
	location = na.array(range(185))
	b1 = bar(location, NUM, width=1, color='c')
	xticks(range(140, 190, 5))
	yticks(range(0, 25000, 1000))
	xlim(135, 190)
	ylim(0, 25000)
	show()

'''
COUNT(num_height, height)
PIC(num_height)

COUNT(num_ave__05, height_ave__05)
PIC(num_ave__05)

COUNT(num_ave__10, height_ave__10)
PIC(num_ave__10)
'''
COUNT(num_ave__25, height_ave__25)
PIC(num_ave__25)
'''
COUNT(num_ave__50, height_ave__50)
PIC(num_ave__50)

COUNT(num_ave__100, height_ave__100)
PIC(num_ave__100)
'''