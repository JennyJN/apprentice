import cv2
import numpy as np
from matplotlib.pyplot import imshow
import os

class Image(object):
	"""wrapper of loading/showing image"""
	def __init__(self, path='', pixel=None):
		if bool(path):
			img = cv2.imread(path)
			b,g,r = cv2.split(img)
			self.img = cv2.merge([r,g,b])

		elif bool(pixel):
			self.img = pixel

		self.size = self.img.shape

	def __call__(self, *args):
		self.show(*args)

	def show(self, *args):
		if bool(args):
			img = cv2.resize(self.img, args)
		else:
			img = self.img

		imshow(img)


def load_folder(folder):
	""" load all images from folder """
	out = []
	files = os.listdir(folder)
	for filename in files:
		if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
			fp = os.path.join(folder, filename)
			img = Image(path=fp)
			out.append(img)

	return out

