#!/Users/dmitrychernyshev/Projects/stepik_python/venv/bin/python3
import sys, re, requests


a_pattern = r"<a (.*)?>"
ref_pattern = r"(.*href\=[\"\'])(.*)([\"\'].*)"
site_pattern = r"(http\:\/\/|https\:\/\/|ftp\:\/\/)?(\w+[\w\.]+)([\/\:])?"
sites = set()

link = input().strip()
res = requests.get(link)

# get all anchors
anchors = re.findall(a_pattern, res.text)
for anchor in anchors:
    href = re.match(ref_pattern, anchor).group(2)
    m_site = re.match(site_pattern, href)
    try:
        site = m_site.group(2)
        sites.add(site)
    except AttributeError:
        pass

for site in sorted(sites):
    print(site)
# for line in sys.stdin:
#     line = line.strip()
#     res = requests.get(line)

#     anchors = re.findall(a_pattern, res.text)
#     print(anchors)
#     for m_url in anchors:
#         url = m_url[1]
#         m_site = re.match(site_pattern, url)
#         if m_site is None:
#             continue
#         site = m_site.group(2)
#         if not site in sites:
#             sites[site] = 1
#         else:
#             sites[site] += 1

# for site in sorted(sites):
#     print(site)
