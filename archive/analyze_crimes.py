#!/Users/dmitrychernyshev/Projects/stepik_python/venv/bin/python3
import csv


def open_csv():
	dct = []
	with open("Crimes.csv") as f:
		rdr = csv.DictReader(f)
		for row in rdr:
			dct.append(row)
	return dct

if __name__ == '__main__':
	crimes = {}

	csv_dict = open_csv()
	for row in csv_dict:
		if row['Primary Type'] in crimes:
			crimes[row['Primary Type']] += 1
		else:
			crimes[row['Primary Type']] = 1
	print(crimes)