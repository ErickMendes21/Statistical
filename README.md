CSV Statistics Analyzer
This Python script allows the user to select a CSV file containing numerical data and then calculates the mean, median, and mode of the dataset.

.Features
File selection via a GUI dialog (using tkinter)

Handles CSV files with a header row

.Computes:

Mean (average)

Median

Mode

.Requirements
Python 3.x
NumPy

.How It Works
A file dialog prompts the user to select a CSV file.

The script reads the file, skipping the header row.

.It calculates:

The average by summing all values and dividing by the number of elements.

The median by sorting the values and finding the middle value(s).

The mode by identifying the most frequent value.

It prints the results to the terminal.

.Installation
Make sure you have Python 3 and NumPy installed:

pip install numpy

.You will be prompted to choose a CSV file. The file must contain only numerical values and a single header row.

.Example CSV Format
value
10
20
20
30
40
