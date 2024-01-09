import xlrd
import json

def xls_to_json(xls_file):
    workbook = xlrd.open_workbook(xls_file)

    sheet = workbook.sheet_by_index(0)

    headers = [cell.value for cell in sheet.row(0)]

    data = []

    for row_index in range(1, sheet.nrows):
        row_values = sheet.row_values(row_index)
        row_dict = dict(zip(headers, row_values))
        data.append(row_dict)

    json_data = json.dumps(data, indent=2)

    return json_data


# Пример
xls_file = "test.xls"
json_output = xls_to_json(xls_file)
print(json_output)
