import csv

def extract_data(file_name):
    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csvreader:
            print(', '.join(row))

extract_data('student_test_scores_extended.csv')