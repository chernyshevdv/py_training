import requests
from lxml import etree

res = requests.get('https://docs.python.org/3/')
print(res.status_code)
print(res.headers['Content-Type'])

parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser)
for element in root.iter("a"):
    print(f"{element.tag} href='{element.attrib['href']}'")