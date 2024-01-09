import csv
import json

def csv_to_json(csv_file):
    data = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            data.append(row)

    json_data = json.dumps(data, indent=2)

    return json_data


# Пример
csv_file = "test.csv"
json_output = csv_to_json(csv_file)
print(json_output)
