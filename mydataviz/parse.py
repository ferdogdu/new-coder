import csv, pprint

MY_FILE = "C:\Users\TOSHIBA\\new-coder\mydataviz\data\sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-line object."""

	# Open CSV file
	opened_file = open(raw_file)

	# Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	# Setup an empty list
	parsed_data = []

	# Skip over the first line of the file for the headers
	fields = csv_data.next()

	# Iterate over each row of the csv file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close CSV file
	opened_file.close()
	
	return parsed_data

def main():
	# Call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")

	# Let's see what the data looks like! We used PrettyPrinter.
	# pprint.pprint(new_data)

	# Write the data in a txt file
	with open("parsed_data.txt", "w") as f:
		for row in new_data:
			for k, v in row.items():
				if k == "Category" and row != new_data[0]:
					f.write("\n" + k + "\t:\t" + v + "\n")
				else:
					f.write(k + "\t:\t" + v + "\n")

if __name__ == "__main__":
	main()