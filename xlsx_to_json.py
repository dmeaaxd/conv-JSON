import openpyxl
import json

def xlsx_to_json(xlsx_file):
    wb = openpyxl.load_workbook(xlsx_file)

    sheet = wb.active

    headers = [cell.value for cell in sheet[1]]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_dict = dict(zip(headers, row))
        data.append(row_dict)

    json_data = json.dumps(data, indent=2)

    return json_data


# Пример
xlsx_file = "test.xlsx"
json_output = xlsx_to_json(xlsx_file)
print(json_output)
