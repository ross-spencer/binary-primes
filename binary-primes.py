from PIL import Image
import argparse
import random

def HEXtoRGB(colorstring):
	#courtesy of code recipes. getrgb from PIL would be better (if it worked)
	colorstring = colorstring.strip()
	if colorstring[0] == '#': colorstring = colorstring[1:]
	r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
	r, g, b = [int(n, 16) for n in (r, g, b)]
	return (r, g, b)

def random_color():
	color_list = ['#4D4DFF', '#67C8FF', '#8D38C9', '#FF0000', '#FFFF00']
	random.seed()
	colorstr = color_list[random.randint(0, 4)]
	return HEXtoRGB(colorstr)

def handleprimes():

	primes = [1,2,3,4,5]
	no_of_primes = len(primes)

	imgx = (no_of_primes * 12 + 12) + 12
	imgy = 51	#maximum width of word * 3 (pixels) + 6 (margin)
	image = Image.new("RGB", (imgx, imgy))
	gx = 0
	
	i = 0
	bin_list = []
	for x in primes:
		no = int(x)
		s = bin(no)
		s = s.lstrip('-0b')
		bin_list.append(s.rjust(15, '0'))	# 15 to make width uniform 
														# TODO: make dynamic
														
														
	gx = 12
	for y in bin_list:
	
		gy = 0
	
		color = random_color()
		
		for z in y:
		
			if z == '0':
				gx+=0
				gy+=3
				
			else:

				for gxx in range(12):
					image.putpixel((gx+gxx, gy), color)
					image.putpixel((gx+gxx, gy+1), color)
					image.putpixel((gx+gxx, gy+2), color)
				
				gx+=0
				gy+=3

		#increment for each word
		gx+=12
		print str(gx)

	image.save("bin.png", "PNG")

def parseCommandLine():
	parser = argparse.ArgumentParser(description='Generate visual binary representations of prime numbers.')
	parser.add_argument('--version', help="Display the version number of the tool", action='version', version='%(prog)s v0.1-BETA')
	args = parser.parse_args()

def main():
	parseCommandLine()
	handleprimes()

if __name__ == "__main__":
    main()