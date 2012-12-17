import argparse

def parseCommandLine():
	parser = argparse.ArgumentParser(description='Tool for the automated generation of digital objects based on the digital signatures documented in the PRONOM database maintained by The National Archives, UK.')
	parser.add_argument('--version', help="Display the version number of the tool", action='version', version='%(prog)s v0.1-BETA')
	args = parser.parse_args()

def main():
	parseCommandLine()

if __name__ == "__main__":
    main()