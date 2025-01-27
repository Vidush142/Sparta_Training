import csv

def extract_data(file_name):
    with open('student_test_scores_extended.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', qoutechar='|')
        for row in csvreader:
            print(', '.join(row))