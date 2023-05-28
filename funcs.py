import csv
from jinja2 import Environment, FileSystemLoader

def clients_to_dict(filename):
    data_dict = {}

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок файла
        for row in reader:
            email = row[1]
            values = [row[0], row[5], row[6], row[7], row[8]]
            if email in data_dict:
                data_dict[email].append(values)
            else:
                data_dict[email] = [values]

    return data_dict

def create_pdf_from_list(value):
    pass

