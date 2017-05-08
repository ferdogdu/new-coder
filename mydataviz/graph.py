import sys

sys.path.append("C:\Users\TOSHIBA\\new-coder\mydataviz")

from parse import parse
from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "C:\Users\TOSHIBA\\new-coder\mydataviz\data\sample_sfpd_incident_all.csv"

data_file = parse(MY_FILE, ",")

def visualize_days(parsed_data):
	"""Visualize data by day of week"""

	# Pythonic list comprehension
	# c = Counter(item["DayOfWeek"] for item in parsed_data) 

	# A for loop instead of a list comprehension
	
	# An empty counter can be constructed with no arguments
	c = Counter()
	
	for item in parsed_data:
		# and populated via the update() method.
		c.update([item["DayOfWeek"]])

	# Separate out the counter to order it correctly when plotting.
	data_list = [
                  c["Monday"],
                  c["Tuesday"],
                  c["Wednesday"],
                  c["Thursday"],
                  c["Friday"],
                  c["Saturday"],
                  c["Sunday"]
                ]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
	plt.plot(data_list)

    # Assign labels to the plot from day_list
	plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph!
    # The PNG file, "Days.png".  This is our graph!
	plt.savefig("Days.png")

    # Close figure
	plt.clf()

def visualize_type(parsed_data):
    """Visualize data by category in a bar graph"""
    
    c = Counter(item["Category"] for item in parsed_data)

	# Set the labels which are based on the keys of our counter.
    labels = tuple(c.keys())

    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, c.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph!
    plt.savefig("Type.png")

    # Close figure
    plt.clf()

def main():
	visualize_days(data_file)
	visualize_type(data_file)

if __name__ == "__main__":
	main()