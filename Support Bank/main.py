from csv_file import CSVAnalyzer
from json_file import JSONAnalyzer
from brain import Brain
import os
import json


#FILE_PATH = r"C:\Users\johan\OneDrive\Documents\Python\Python\Support Bank\Transactions2014.csv"
#FILE_PATH = r"C:\Users\johan\OneDrive\Documents\Python\Python\Support Bank\DodgyTransactions2015.csv"
FILE_PATH = r"C:\Users\johan\OneDrive\Documents\Python\Python\Support Bank\Transactions2013.json"


# Check the file extensions
def check_file_extension(FILE_PATH, extension):
    _, file_ext = os.path.splitext(FILE_PATH)
    return file_ext.lower() == extension.lower()


# CSV file
if check_file_extension(FILE_PATH, '.csv'):
    csv_analyzer = CSVAnalyzer(FILE_PATH)

    # Checks the amount and date field to see if all the data is valid, if not, it displays the affected rows
    # and the program stops
    flag = csv_analyzer.check_amount_fields_valid()
    flag = csv_analyzer.check_date_fields_valid()

    if not flag:
        print("\n*** Change the above lines' values first ***\n")
    else:
        brain = Brain(csv_analyzer)
        brain.csv_loop()


# JSON file
elif check_file_extension(FILE_PATH, '.json'):
    with open(FILE_PATH, 'r') as file:
        data = json.load(file)
    json_analyzer = JSONAnalyzer(data)
    flag = json_analyzer.check_amount_fields_valid()
    flag = json_analyzer.check_date_fields_valid()

    if not flag:
        print("\n*** Change the above lines' values first ***\n")
    else:
        brain = Brain(json_analyzer)
        brain.json_loop()


else:
    print(f'The file {FILE_PATH} has an unsupported extension.')




