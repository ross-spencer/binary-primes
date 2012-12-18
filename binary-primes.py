from PIL import Image
import argparse
import random
import math

def HEXtoRGB(colorstring):
	#courtesy of code recipes. getrgb from PIL would be better (if it worked)
	colorstring = colorstring.strip()
	if colorstring[0] == '#': colorstring = colorstring[1:]
	r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
	r, g, b = [int(n, 16) for n in (r, g, b)]
	return (r, g, b)

def random_color():
	color_list = ['#4D4DFF', '#67C8FF', '#8D38C9', '#FF0000', '#FFFF00']
	#color_list = ['#C21F1F', '#8C0E0E', '#470808', '#D11111', '#F21313']
	random.seed()
	colorstr = color_list[random.randint(0, len(color_list)-1)]
	return HEXtoRGB(colorstr)

def load_list():

	prime_list = []
	f = open('primes-list.txt', 'r')
	x = 0
	for line in f:
		prime_list.append(int(line))	#need ints not strings
		x+=1
	
	#prime_list = [2,3,5,7,11]
	return prime_list

def handleprimes(args):

	primes = load_list()
	no_of_primes = len(primes)

	binary_int_width = int(math.ceil(math.log(max(primes), 2)))	#zeros needed
	y_pixels = 3
	y_margin_bottom = 12
	y_margin_top = 12

	x_pixels = 3
	x_margin_left = 24
	x_margin_right = 24


	if args.tiled == False:
		imgx = (no_of_primes * x_pixels) + x_margin_left + x_margin_right
		imgy = (binary_int_width * y_pixels) + y_margin_bottom + y_margin_top
	elif args.tiled == True:
		imgx = 1000
		imgy = 1010
		
	image = Image.new("RGB", (imgx, imgy))
	gx = 0
	
	i = 0
	bin_list = []
	for x in primes:
		no = int(x)
		s = bin(no)
		s = s.lstrip('-0b')
		bin_list.append(s.rjust(binary_int_width, '0'))

	gx = x_margin_left
	loop = 0
	
	for y in bin_list:	
		if args.tiled == True:
			gy = y_margin_top + 50 * loop
		else:
			gy = y_margin_top
			
		color = random_color()
		for z in y:
			if z == '0':
				gx+=0
				gy+=y_pixels
			else:
				for gxx in range(x_pixels):
					for gyy in range(y_pixels):
						image.putpixel((gx+gxx, gy+gyy), color)
					
				gx+=0
				gy+=y_pixels

		if args.tiled == True:
			if gx >= 990:
				gx=0
				loop+=1
			else:
				gx += x_pixels
		else:
			gx+=x_pixels	#increment for each word

	image.save("bin.png", "PNG")

def parseCommandLine():
	parser = argparse.ArgumentParser(description='Generate visual binary representations of prime numbers.')
	parser.add_argument('--version', help="display the version number of the tool", action='version', version='%(prog)s v0.1-BETA')
	parser.add_argument('--tiled', help="tile the output", action='store_true')
	args = parser.parse_args()
	return args

def main():
	args = parseCommandLine()
	handleprimes(args)

if __name__ == "__main__":
    main()