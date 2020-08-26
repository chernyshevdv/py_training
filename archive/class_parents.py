#!/Users/dmitrychernyshev/Projects/stepik_python/venv/bin/python3
import json


classes = []
relations = []

def calc_descendants(parent, visited=None):
	global relations
	count = 0
	if visited is None:
		visited = set()
		count = 1 # I'm (or Object is) a parent of myself
		visited.add(parent)
	for row in relations:
		if row['parent'] == parent and not row['child'] in visited:
			count += 1
			visited.add(row['child'])
			count += calc_descendants(row['child'], visited)

	return count


def append_class(item):
	global classes
	if not item in classes:
		classes.append(item)


def append_relation(parent, child):
	global relations
	found = False
	for row in relations:
		if row['parent'] == parent and row['child'] == 'child':
			found = True
			break
	if not found:
		relations.append({'parent': parent, 'child': child})

data = json.loads(input())

for row in data:
	child = row['name']
	append_class(child)
	for parent in row['parents']:
		append_class(parent)
		append_relation(parent, child)

for item in sorted(classes):
	print(f"{item} : {calc_descendants(item)}")