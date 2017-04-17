'''
This file contains the class for reading text files.
Please fill up the functions oneHot and convertHot.
'''
import numpy as np
import random
class textDataLoader(object):
	def __init__(self, datapath):
		self.nFeats = 128
		print 'Loading Data'
		self.D = open(datapath,'r').read()
		self.nChars = len(self.D)
		self.N = [ord(c) for c in self.D]
		self.D_oneHot = np.array([self.oneHot(n) for n in self.N])

	def oneHot(self, character):
		'''
		In this function you need to output a one hot encoding of the ASCII character.
		'''
	
	def convertHot(self, string_l):
		'''
		In this function, you will need to write a piece of code that converts a string
		to a numpy array of one hot representation.
		'''
		
	def getBatch(self, batch_size, max_length):
		input_b = np.zeros([batch_size, max_length, self.nFeats])
		output_b =  np.zeros([batch_size, max_length, self.nFeats])
		for i in range(batch_size):
			r = random.randint(0,self.nChars-2-max_length)
			input_b[i] = self.D_oneHot[r:r+max_length]
			output_b[i] = self.D_oneHot[r+1:r+1+max_length]
		return input_b, output_b
