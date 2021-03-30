import argparse
import time
import calendar

parser = argparse.ArgumentParser()
parser.add_argument('--search', type=str, help="search for all games with the word ")
parser.add_argument('--file', type=str, help=" output to csv file")
parser.add_argument('--showdlc', type=bool, help="option to show DLC for returned games")
parser.add_argument('--gid', type=str, help="Show details of a specific game.")
args = parser.parse_args()
search = args.search
outputFile = args.file
showdlc = args.showdlc
gid= args.gid
apikey = 'ff048b3a6e122abaa059c090523b2ce88c5e0c53'
search_endpoint='https://www.giantbomb.com/api/games/'
api_endpoint='https://www.giantbomb.com/api'
