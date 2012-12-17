import argparse

def parseCommandLine():
	parser = argparse.ArgumentParser(description='Generate visual binary representations of prime numbers.')
	parser.add_argument('--version', help="Display the version number of the tool", action='version', version='%(prog)s v0.1-BETA')
	args = parser.parse_args()

def main():
	parseCommandLine()

if __name__ == "__main__":
    main()