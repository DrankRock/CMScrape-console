import sys
import argparse
import csv

sys.path.insert(1, './back')

from flaresolverr import start_flaresolverr, stop_flaresolverr
from check_dependencies import check_docker_installed, update_libseccomp
from request import get, download
from utils import temp_file
from scraper import cm_parser
from bs4 import BeautifulSoup
from datetime import datetime

def now():
	current_time = datetime.now()
	return str(current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

# Check arguments
parser = argparse.ArgumentParser(description='Cardmarket information scraper from a list of links')
parser.add_argument('-i','--input', help='Input file or url of the input file', required=True)
parser.add_argument('-o', '--output', help="Output file", required=True)
args = vars(parser.parse_args())

if args['input'].startswith("https"):
	inputFile = temp_file(args['input'])
else:
	inputFile = args['input']

IMAGES_PATH = "./img/"

# check dependencies
check_docker_installed()
update_libseccomp()

# launch flaresolverr
start_flaresolverr()
links = []
count = 1
try :
	with open(inputFile, 'r') as infile:
		for line in infile:
			links.append(line.strip())
	with open(args['output'], 'w', newline='') as outfile:
		csv_writer = csv.writer(outfile)
		csv_writer.writerow(["title", "expansion", "rarity", "from", "trend", "30 days", "7 days", "1 day", "url", "image name"])
		for link in links :
			try:
				stuck = False
				stuckCounter = 1
				response = get(link)
				while (response.status_code == 429):
					if not stuck:
						print("[BLOCKED] - ", now())
						stuckCounter += 1
					time.sleep(10)
					response = get(link)
				if stuck :
					print("[UNBLOCKED] - ", now())
				print("[LOG] - {}".format(count))
				parsed = cm_parser(line, response)
				img_name = IMAGES_PATH+parsed[0].replace(" ", "_")+".jpg"
				# download(parsed[-1], img_name, response.cookies, response.headers)
				csv_writer.writerow([parsed[0], parsed[3][0], parsed[2][0], parsed[1][0], parsed[1][1], parsed[1][2], parsed[1][3], parsed[1][4], link])
			except:
				print("[BAD PAGE] : ", link)
			
finally:
	# stop flaresolverr
	stop_flaresolverr()
