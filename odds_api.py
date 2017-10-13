import sys
import requests
import json, ast

# https://stackoverflow.com/questions/23450534/how-to-call-python-function-from-nodejs
HOST = "https://86qbtjzii8.execute-api.ap-southeast-2.amazonaws.com"
HEADERS = {"x-api-key": "cmiuIEQhnc3bnlEV5eFlQ3huxcoBIE954wxS7VHI", "Accept": "application/json"}


def main():
	sport = "NFL"
	teams = "Jacksonville Jaguars_Pittsburgh Steelers"

	odds = [0,0]
	num_sites = 0

	endpoint = "/live_uk/odds/"
	#r = requests.get(HOST + endpoint + "NFL", headers=HEADERS)
	#r = json.loads(r.text)

	#DELETE
	r = {u'sport_display': u'NFL', u'status': u'Pending', u'sites': {u'pinnacle': {u'odds': {u'h2h': [u'3.97', u'1.29']}, u'last_update': 1507330292}, u'tonybet': {u'odds': {u'h2h': [u'4.25', u'1.22']}, u'last_update': 1507330322}, u'betfair': {u'odds': {u'h2h': [u'4.04', u'1.28'], u'h2h_lay': [u'4.40', u'1.32']}, u'last_update': 1507330293}, u'skybet': {u'odds': {u'h2h': [u'4.00', u'1.25']}, u'last_update': 1507330335}, u'unibet': {u'odds': {u'h2h': [u'4.25', u'1.24']}, u'last_update': 1507330337}, u'williamhill': {u'odds': {u'h2h': [u'3.80', u'1.28']}, u'last_update': 1507330324}, u'ladbrokes': {u'odds': {u'h2h': [u'4.00', u'1.25']}, u'last_update': 1507330323}}, u'participants': [u'Jacksonville Jaguars', u'Pittsburgh Steelers'], u'sport': u'NFL', u'commence': u'1507482000'} 

	#for key, val in r["data"]["events"][teams]["sites"].iteritems():
	for key, d in r["sites"].iteritems():
		sum = float(d["odds"]["h2h"][0]) + float(d["odds"]["h2h"][1])
		odds[0] = odds[0] + float(d["odds"]["h2h"][0]) / sum
		odds[1] = odds[1] + float(d["odds"]["h2h"][1]) / sum
		num_sites += 1
	odds[0] = odds[0] / num_sites
	odds[1] = odds[1] / num_sites
	print odds

if __name__ == "__main__":
	main()
