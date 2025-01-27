import csv

def extract_data(file_name):
    with open(file_name, newline='') as csvfile:
        student_data_dict = csv.DictReader(csvfile)
        for row in student_data_dict:
            print(row)

    return student_data_dict

def transform_data(file_name):
    input_data = extract_data(file_name)
    new_columns = ["Name", "Math Score", "English Score", "Science Score", "Art Score", "History Score"]
    result_dict = {x:input_data[x] for x in new_columns}

    for row in result_dict:
        print(row)



transform_data('student_test_scores_extended.csv')