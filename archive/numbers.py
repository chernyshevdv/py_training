#!/Users/dmitrychernyshev/Projects/stepik_python/venv/bin/python3
import json
import sys
import requests


params = {
	'default': 'boring',
	'fragment': ''
	}

for line in sys.stdin:
	line = line.strip()
	url = "http://numbersapi.com/" + line + "/math"

	res = requests.get(url, params=params)
	print('Interesting' if res.text != 'boring' else 'Boring')

