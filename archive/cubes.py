from lxml import etree

cubes = {}


def increment_cube(color, level):
    global cubes
    if color not in cubes:
        cubes[color] = 0
    cubes[color] += level


def calculate(element, level=1):
    global cubes
    for child in element:
        increment_cube(child.attrib['color'], level+1)
        calculate(child, level+1)


parser = etree.XMLParser()
root = etree.fromstring(input(), parser)
print(f"Parsed input. Root element: {root.tag}")

cubes[root.attrib['color']] = 1
calculate(root, 1)

print(f"{cubes['red']} {cubes['green']} {cubes['blue']}")