#!/Users/dmitrychernyshev/Projects/stepik_python/venv/bin/python3
import json
import sys
import requests

xapp_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI1ZjQyNmI4ZjNmMTNkOTAwMGRkYWEyYjMiLCJleHAiOjE1OTg3OTMyMzIsImlhdCI6MTU5ODE4ODQzMiwiYXVkIjoiNWY0MjZiOGYzZjEzZDkwMDBkZGFhMmIzIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjVmNDI2YjkwODYwNGQ3MDAwZWVjNzA3ZiJ9.zCZuv6ByiXty4Tn7mS3-Krq3SpuKQ82ETGUdnBS6hHs"

headers = {
	'X-Xapp-Token': xapp_token
}

data = {}
for line in sys.stdin:
	line = line.strip()
	url = "https://api.artsy.net/api/artists/" + line

	res = requests.get(url, headers=headers)
	artist = res.json()
	data[artist['sortable_name']] = artist['birthday']

sorted_by_year = sorted(data.items(), key=lambda kv: str(kv[1])+kv[0])

for item in sorted_by_year:
	print(item[0])